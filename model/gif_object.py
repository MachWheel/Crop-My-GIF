from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from os.path import splitext

from PIL import Image
from imageio import v3 as iio
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.crop import crop
from screeninfo import get_monitors

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
        self.size = _get_img_size(file)
        self.resize_factor = self._get_resize()
        self.frames = _load_frames(file, self.resize_factor)
        self.n_frames = len(self.frames)
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
        box = self._apply_factor(box)
        gif = VideoFileClip(self.file).subclip(0)
        cropped = crop(gif, *box)
        cropped.write_gif(filename=output, program='ffmpeg')
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


    def _apply_factor(self, box: CropBox) -> CropBox:
        """
        Applies the gif object resize factor
        into the crop coordinates selected by
        the user and returns it as
        **CropBox(x0, y0, x1, y1)**
        """
        return CropBox(*[int(n / self.resize_factor) for n in box])


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


def _get_img_size(file) -> Pixels:
    """
    Returns the image file size as
    **Pixels(x, y)**
    """
    gif_img = Image.open(file)
    return Pixels(*gif_img.size)


def _load_frames(file: str, resize=1.0) -> list[bytes]:
    """
    Loads all gif frames into memory using
    multiple threads and returns it's
    contents as a *list of bytes*.
    """
    frames = iio.imiter(file)
    with ThreadPoolExecutor() as e:
        if resize == 1.0:
            results = [e.submit(_load_to_ram, frame)
                       for frame in frames]
        else:
            results = [e.submit(_resize_to_ram, frame, resize)
                       for frame in frames]
    return [data.result() for data in results]


def _load_to_ram(img: iio) -> bytes:
    """
    Loads a gif frame into memory and
    return it's contents as *bytes*.
    """
    with BytesIO() as output:
        iio.imwrite(output, img, format_hint='.png')
        return output.getvalue()


def _resize_to_ram(img: iio, factor: float) -> bytes:
    """
    Resizes a gif frame and loads it
    into memory, returning it's content
    as *bytes*.
    """
    img = Image.fromarray(img)
    width = int(img.size[0] * factor)
    height = int(img.size[1] * factor)
    img = img.resize(
        resample=Image.Resampling.LANCZOS,
        reducing_gap=1.0,
        size=(width, height)
    )
    with BytesIO() as output:
        img.save(output, format='png')
        return output.getvalue()
