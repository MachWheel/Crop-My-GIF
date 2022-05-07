from PIL import Image
from screeninfo import get_monitors

from model.units import Pixels


def get_monitor_area(factor=0.7) -> Pixels:
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


def get_gif_info(file) -> tuple[Pixels, int]:
    """
    Returns the gif file size as
    **Pixels(x, y)**, and its number
    of frames as **int**
    """
    gif_img = Image.open(file)
    n_frames = gif_img.n_frames
    return Pixels(*gif_img.size), n_frames


def _load_frames() -> list[bytes]:
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
