from concurrent.futures import ThreadPoolExecutor, Future
from os.path import splitext, isfile

from imageio import v3 as iio
from moviepy.video.fx.crop import crop
from moviepy.video.io.VideoFileClip import VideoFileClip

import model
import views
from controllers import _msgs


class Cropper:
    """
    Controller responsible for cropping and exporting
    a given GIF file.
    """
    def __init__(self, info: model.GifInfo, box: model.units.CropBox, preserve_fps: bool):
        """
        Initializes a new Cropper object.

        :param info: Object containing the GIF file information
        :type info: model.GifInfo

        :param box: selected crop coordinates as
            a named tuple: CropBox(x0, y0, x1, y1)
        :type box: model.units.CropBox

        :param preserve_fps: Preserves the input frame rate if True
        :type preserve_fps: bool
        """
        self._info = info
        self._box = box
        self._preserve_fps = preserve_fps
        self._export_fps = 10.0 if preserve_fps else 20.0

    def export_gif(self) -> str | None:
        """
        Exports a cropped GIF file according to current instance values.

        :returns: The output file path if successful
        :rtype: str | None
        """
        in_name = splitext(self._info.gif_file)[0]
        output = f"{in_name}_CROP.gif"
        if not self._run_export(output):
            return None
        if not self._preserve_fps:
            return output
        self._fix_export_fps(output)
        return self._run_export(output)

    def _run_export(self, output: str) -> str | None:
        """
        Submits the GIF file writing task as a thread,
        displaying its progress in a popup window.

        :returns: The output file path if successful
        :rtype: str | None
        """
        with ThreadPoolExecutor() as e:
            task = e.submit(self._write_task, output)
            _show_running(task)
            return task.result()

    def _write_task(self, output) -> str | None:
        """
        Writes the cropped GIF file output.

        :returns: The output file path if successful
        :rtype: str | None
        """
        obj = VideoFileClip(self._info.gif_file).subclip(0)
        obj = crop(obj, *self._box)
        fps = self._export_fps
        obj.write_gif(filename=output, program='ffmpeg', fps=fps)
        obj.close()
        if isfile(output):
            return output
        return None

    def _fix_export_fps(self, output) -> None:
        """
        Sets cropper _export_fps value as the input
        frame rate by reading the first output number
        of frames.
        """
        in_n_frames = self._info.n_frames
        out_n_frames = 0
        for _ in iio.imiter(output):
            out_n_frames += 1
        fps = (in_n_frames * self._export_fps) / out_n_frames
        self._export_fps = fps


def _show_running(task: Future[str]) -> None:
    """
    Displays the running exporting task progress
    in a popup window.

    :param task: Running export task
    :type task: Future[str]
    """
    i, reload_i, bar_end = 0, 199, 200
    view = views.PROGRESS(importing=False, bar_end=bar_end)
    while task.running():
        view.read(timeout=10)
        if i == reload_i:
            i = 0
            view['-TXT-'].update(_msgs.SLOW_EXPORTING())
        view['-PROG-'].update(current_count=(i + 1))
        i += 1
    view.close()
