from concurrent.futures import ThreadPoolExecutor, Future
from os.path import splitext

from moviepy.video.fx.crop import crop
from moviepy.video.io.VideoFileClip import VideoFileClip

from model.units import CropBox
from views import PROGRESS_VIEW
from ._msgs import SLOW_EXPORTING
from .gif_info import GifInfo


class GifCropper:
    def __init__(self, gif_info: GifInfo, box: CropBox):
        self.info = gif_info
        self.box = box

    def export_gif(self):
        """
        Executes a threaded call to GifCropper **_crop_file()**
        function, which crops the current gif file according to
        instance attribute **crop_box: CropBox(x0, y0, x1, y1)**.
        Returns the output file name.
        """
        with ThreadPoolExecutor() as e:
            task = e.submit(self._crop_file)
            _show_progress(task)
            result = task.result()
        return result

    def _crop_file(self) -> str:
        file = self.info.gif_file
        output = f"{splitext(file)[0]}_CROP.gif"
        gif = VideoFileClip(file).subclip(0)
        cropped = crop(gif, *self.box)
        cropped.write_gif(filename=output, program='ffmpeg', fps=30)
        return output


def _show_progress(task: Future[str]):
    bar_max = 100
    prog, txt = 0, 0
    view = PROGRESS_VIEW()
    while task.running():
        view.read(timeout=10)
        if prog == bar_max - 1:
            prog = 0
            view['-TXT-'].update(SLOW_EXPORTING())
        view['-PROG-'].update(current_count=(prog + 1))
        prog += 1
    view.close()
