from concurrent.futures import ThreadPoolExecutor, Future
from os.path import splitext
from typing import Any

from imageio import v3 as iio
from moviepy.video.fx.crop import crop
from moviepy.video.io.VideoFileClip import VideoFileClip

import model
from . import _msgs
from views import PROGRESS_VIEW


class GifCropper:
    def __init__(self, info: model.GifInfo, box: model.units.CropBox, preserve_fps: bool):
        """
        Initializes a new GifCropper instance.
        Args:
            info: GifInfo:
                Object containing the gif file
                information.

            box: CropBox(x0, y0, x1, y1):
                Coordinates to crop the file.

            preserve_fps : bool:
                If true the output will have the
                same frame rate as the input.
        """
        self.info = info
        self.box = box
        self.preserve_fps = preserve_fps

    def export_gif(self):
        """
        Executes a threaded call to GifCropper
        function **_crop_file()**.

        :return: output gif file path.
        """
        with ThreadPoolExecutor() as e:
            task = e.submit(self._crop_file)
            TASK_PROGRESS(task)
            result = task.result()
        return result

    def _crop_file(self) -> str:
        """
        Crops the current gif file according to
        **info** and **box** instance attributes.

        :return: output gif file path.
        """
        file = self.info.gif_file
        output = f"{splitext(file)[0]}_CROP.gif"
        gif_obj = VideoFileClip(file).subclip(0)
        gif_obj = crop(gif_obj, *self.box)
        output = _write_output(output, gif_obj)
        if self.preserve_fps:
            in_n_frames = self.info.n_frames
            fps = _calculate_real_fps(output, in_n_frames)
            output = _write_output(output, gif_obj, fps)
        gif_obj.close()
        return output


_DEFAULT_FPS = 20.0

def _write_output(output, obj, fps=_DEFAULT_FPS) -> Any:
    """
    Writes the output gif file and returns its path.

      **output**:
        Output gif file path.
      **obj**:
        MoviePy clip object to write the output gif file.
      **fps**:
        Frame rate of the output gif file. (default=20.0)
    """
    obj.write_gif(filename=output, program='ffmpeg', fps=fps)
    return output

def _calculate_real_fps(output, in_n_frames: int) -> float:
    """
    Calculates and returns the exact input gif
    frame rate based on the output number of frames.

      output:
        The output gif file path.
      in_n_frames:
        The input gif file number of frames.
    """
    out_n_frames = 0
    for _ in iio.imiter(output):
        out_n_frames += 1
    fps = (in_n_frames * _DEFAULT_FPS) / out_n_frames
    return fps

def TASK_PROGRESS(task: Future[str]):
    bar_end, reload_i, i = 100, 99, 0
    view = PROGRESS_VIEW(importing=False, bar_end=bar_end)
    while task.running():
        view.read(timeout=10)
        if i == reload_i:
            i = 0
            view['-TXT-'].update(_msgs.SLOW_EXPORTING())
        view['-PROG-'].update(current_count=(i + 1))
        i += 1
    view.close()
