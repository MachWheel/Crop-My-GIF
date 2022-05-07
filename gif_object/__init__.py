from concurrent.futures import ThreadPoolExecutor
from os.path import splitext

from moviepy.video.fx.crop import crop
from moviepy.video.io.VideoFileClip import VideoFileClip

from ._export import export_progress
from ._load import get_resize_factor, get_gif_info, load_gif_frames
from model.units import Pixels, CropBox


class GifObject:
    """
    Loads a gif file into memory and
    represents it size and frames.
    """
    def __init__(self, file):
        """
        Initializes an instance of GifObject containing
        *file, size, resize_factor, frames and n_frames*
        attributes.
        """
        self.gif_file = file
        self.size, self.n_frames = get_gif_info(file)
        self.resize_factor = get_resize_factor(self)
        self.frames = load_gif_frames(self)
        print(len(self.frames), 'frames loaded')


    @property
    def display_size(self) -> Pixels:
        """
        Returns gif current displaying
        size as **Pixels(x, y)**
        """
        width = int(self.size.x * self.resize_factor)
        height = int(self.size.y * self.resize_factor)
        return Pixels(width, height)


    def crop_export(self, box: CropBox):
        with ThreadPoolExecutor() as e:
            task = e.submit(
                self._crop_file, box
            )
            export_progress(task)
            result = task.result()
        return result


    def _crop_file(self, box: CropBox) -> str:
        """
        Crops current gif file within the specified
        coordinates **CropBox(x0, y0, x1, y1)**
        and returns output file name.
        """
        output = f"{splitext(self.gif_file)[0]}_CROP.gif"
        box = self._apply_crop_factor(box)
        gif = VideoFileClip(self.gif_file).subclip(0)
        cropped = crop(gif, *box)
        cropped.write_gif(filename=output, program='ffmpeg', fps=30)
        return output


    def _apply_crop_factor(self, box: CropBox) -> CropBox:
        """
        Applies the gif object resize factor
        into the crop coordinates selected by
        the user and returns it as
        **CropBox(x0, y0, x1, y1)**
        """
        return CropBox(*[int(n / self.resize_factor) for n in box])
