from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

from PIL import Image
from imageio.v3 import imiter, imwrite
from numpy import ndarray

import model
import views


class Frames:
    """
    Holds individual GIF file frames as a list of bytes
    """
    def __init__(self, gif_info: model.GifInfo):
        """
        Initializes a new Frames object, which loads the GIF file frames

        :param gif_info: Object containing the GIF file information
        :type gif_info: model.GifInfo
        """
        self.loaded = _load_all(gif_info)


def _load_all(info: model.GifInfo) -> list[bytes]:
    """
    Returns all GIF file frames into a list of bytes.

    :param info: Object containing the GIF file information
    :type info: model.GifInfo
    """
    frames = imiter(info.gif_file)
    prog = views.PROGRESS(bar_end=info.n_frames)
    i, results, key = 0, [], '-PROG-'
    with ThreadPoolExecutor() as e:
        for frame in frames:
            prog.read(timeout=10)
            prog[key].update(i + 1)
            results.append(e.submit(_load, frame, info))
            i += 1
        prog.close()
    return [frame.result() for frame in results]


def _load(frame: ndarray, info: model.GifInfo) -> bytes:
    """
    Returns a GIF file frame as bytes

    :param frame: Frame to be loaded
    :type frame: numpy.ndarray

    :param info: Object containing the GIF file information
    :type info: model.GifInfo
    """
    if info.resize_factor == 1.0:
        return _png_load(frame)
    return _png_resize_load(frame, info)


def _png_load(frame: ndarray) -> bytes:
    """
    Loads a GIF frame to .png and returns it as bytes

    :param frame: Frame to be loaded
    :type frame: numpy.ndarray
    """
    with BytesIO() as output:
        imwrite(output, frame, format_hint='.png')
        return output.getvalue()


def _png_resize_load(frame: ndarray, info: model.GifInfo) -> bytes:
    """
    Loads a GIF frame, while resizing it, to a .png bytes

    :param frame: Frame to be loaded
    :type frame: numpy.ndarray

    :param info: Object containing the GIF file information
    :type info: model.GifInfo

    :return: .png contents
    :rtype: bytes
    """
    frame = Image.fromarray(frame).resize(
        resample=Image.Resampling.LANCZOS,
        reducing_gap=1.0,
        size=info.display_size
    )
    with BytesIO() as output:
        frame.save(output, format='png')
        return output.getvalue()
