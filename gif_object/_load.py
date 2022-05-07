from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from typing import TYPE_CHECKING

from PIL import Image
from screeninfo import get_monitors
from imageio import v3 as iio

from model.units import Pixels
from view import LOADING
if TYPE_CHECKING:
    from gif_object import GifObject


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


def get_resize_factor(gif_obj: GifObject) -> float:
    """
    Gets the optimal gif display resize factor
    as a float number.
    """
    screen = _get_monitor_area()
    x, y = gif_obj.size.x, gif_obj.size.y
    if x <= screen.x and y <= screen.y:
        return 1.0
    factor_x: float = (screen.x / gif_obj.size.x)
    factor_y: float = (screen.y / gif_obj.size.y)
    return min(factor_x, factor_y)


def get_gif_info(file) -> tuple[Pixels, int]:
    """
    Returns the gif file size as
    **Pixels(x, y)**, and its number
    of frames as **int**
    """
    gif_img = Image.open(file)
    n_frames = gif_img.n_frames
    return Pixels(*gif_img.size), n_frames


def load_gif_frames(gif_obj: GifObject) -> list[bytes]:
    """
    Loads all gif frames into memory using
    multiple threads and returns it's
    contents as a *list of bytes*.
    """
    frames = iio.imiter(gif_obj.gif_file)
    with ThreadPoolExecutor() as e:
        i, results = 0, []
        for frame in frames:
            results.append(e.submit(frame_to_ram, frame, gif_obj))
            LOADING('loading', i, gif_obj.n_frames)
            i += 1
    return [data.result() for data in results]


def frame_to_ram(frame: iio, gif_obj: GifObject) -> bytes:
    """
    Resizes a gif frame if necessary
    and loads it into memory, returning
    it's contents as *bytes*.
    """
    if gif_obj.resize_factor == 1.0:
        with BytesIO() as output:
            iio.imwrite(output, frame, format_hint='.png')
            return output.getvalue()
    else:
        frame = Image.fromarray(frame)
        frame = frame.resize(
            resample=Image.Resampling.LANCZOS,
            reducing_gap=1.0,
            size=gif_obj.display_size
        )
        with BytesIO() as output:
            frame.save(output, format='png')
            return output.getvalue()
