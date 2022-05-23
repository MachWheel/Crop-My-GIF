import screeninfo
from PIL import Image

from .units import Pixels


class GifInfo:
    """
    Holds GIF file information related to its
    directory, graphical size and number of frames.
    """
    def __init__(self, file):
        """
        Initializes a new GifInfo object.

        :param file: GIF file path
        :type file: str
        """
        gif = Image.open(file)
        size = Pixels(*gif.size)
        self.gif_file = file
        self.size = size
        self.resize_factor = _get_resize_factor(size)
        self.n_frames: int = gif.n_frames

    @property
    def display_size(self) -> Pixels:
        """
        :return: Current displaying GIF width and height
            as a named tuple of Pixels(x, y)
        :rtype: model.units.Pixels
        """
        width = int(self.size.x * self.resize_factor)
        height = int(self.size.y * self.resize_factor)
        return Pixels(width, height)


def _get_resize_factor(gif_size: Pixels) -> float:
    """
    DESCRIPTION

    :param gif_size: GIF file width and height as a
        named tuple of Pixels(x, y)
    :type gif_size: model.units.Pixels

    :return: GIF display resize factor as a float value
    :rtype: float
    """
    usable: Pixels = _usable_area()
    if gif_size.x <= usable.x and gif_size.y <= usable.y:
        return 1.0
    else:
        x_resize: float = (usable.x / gif_size.x)
        y_resize: float = (usable.y / gif_size.y)
        return min(x_resize, y_resize)

def _usable_area(default: float = 0.7) -> Pixels:
    """
    :param default: Optional: the default display
        usable area as a float value.
    :type default: flot

    :return: The usable width and height of the smallest
        monitor as a named tuple of Pixels(x, y)
    :rtype: model.units.Pixels
    """
    w = h = 10 ** 10
    for monitor in screeninfo.get_monitors():
        mw, mh = monitor.width, monitor.height
        if mw < w and mh < h:
            w, h = mw, mh
    return Pixels(
        x=int(w * default),
        y=int(h * default)
    )
