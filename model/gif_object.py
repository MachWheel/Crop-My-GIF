from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from os.path import splitext

from PIL import Image
from imageio import v3 as iio
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.crop import crop
from screeninfo import get_monitors

from view import LOADING, EXPORT_PROGRESS
from .units import Pixels, CropBox


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
        self.file = file
        self.size, self.n_frames = _get_gif_info(file)
        self.resize_factor = self._get_resize()
        self.frames = self._load_frames()
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


    def crop_gif(self, box: CropBox) -> str:
        """
        Crops current gif file within the specified
        coordinates **CropBox(x0, y0, x1, y1)**
        and returns output file name.
        """
        output = f"{splitext(self.file)[0]}_CROP.gif"
        box = self._apply_crop_factor(box)
        gif = VideoFileClip(self.file).subclip(0)
        cropped = crop(gif, *box)
        cropped.write_gif(filename=output, program='ffmpeg', fps=30)
        return output


    def _get_resize(self) -> float:
        """
        Gets the optimal gif display resize factor
        as a float number.
        """
        screen = _get_monitor_area()
        x, y = self.size.x, self.size.y
        if x <= screen.x and y <= screen.y:
            return 1.0
        factor_x: float = (screen.x / self.size.x)
        factor_y: float = (screen.y / self.size.y)
        return min(factor_x, factor_y)


    def _apply_crop_factor(self, box: CropBox) -> CropBox:
        """
        Applies the gif object resize factor
        into the crop coordinates selected by
        the user and returns it as
        **CropBox(x0, y0, x1, y1)**
        """
        return CropBox(*[int(n / self.resize_factor) for n in box])


    def _load_frames(self) -> list[bytes]:
        """
        Loads all gif frames into memory using
        multiple threads and returns it's
        contents as a *list of bytes*.
        """
        frames = iio.imiter(self.file)
        with ThreadPoolExecutor() as e:
            i, results = 0, []
            for frame in frames:
                results.append(e.submit(self._frame_to_ram, frame))
                LOADING('loading', i, self.n_frames)
                i += 1
        return [data.result() for data in results]


    def _frame_to_ram(self, img: iio) -> bytes:
        """
        Resizes a gif frame if necessary
        and loads it into memory, returning
        it's contents as *bytes*.
        """
        if self.resize_factor == 1.0:
            with BytesIO() as output:
                iio.imwrite(output, img, format_hint='.png')
                return output.getvalue()
        else:
            img = Image.fromarray(img)
            img = img.resize(
                resample=Image.Resampling.LANCZOS,
                reducing_gap=1.0,
                size=self.display_size
            )
            with BytesIO() as output:
                img.save(output, format='png')
                return output.getvalue()


    def crop_export(self, box: CropBox):
        with ThreadPoolExecutor() as e:
            task = e.submit(
                self.crop_gif, box
            )
            EXPORT_PROGRESS(task, self.n_frames)
            result = task.result()
        return result


def _get_monitor_area(factor=0.7) -> Pixels:
    """
    Gets the available monitor display
    resolution for the gif object.
    """
    w, h = 10000, 10000
    for m in get_monitors():
        if m.width < w and m.height < h:
            w, h = m.width, m.height
    w, h = int(w * factor), int(h * factor),
    return Pixels(w, h)


def _get_gif_info(file) -> tuple[Pixels, int]:
    """
    Returns the gif file size as
    **Pixels(x, y)**, and its number
    of frames as **int**
    """
    gif_img = Image.open(file)
    n_frames = gif_img.n_frames
    return Pixels(*gif_img.size), n_frames
