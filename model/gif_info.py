import screeninfo
from PIL import Image

from .units import Pixels


class GifInfo:
    def __init__(self, file):
        gif = Image.open(file)
        size = Pixels(*gif.size)
        self.gif_file = file
        self.size = size
        self.resize_factor = _get_resize_factor(size)
        self.n_frames: int = gif.n_frames

    @property
    def display_size(self) -> Pixels:
        width = int(self.size.x * self.resize_factor)
        height = int(self.size.y * self.resize_factor)
        return Pixels(width, height)


def _get_resize_factor(gif_size: Pixels) -> float:
    usable: Pixels = _usable_area()
    if gif_size.x <= usable.x and gif_size.y <= usable.y:
        return 1.0
    else:
        x_resize: float = (usable.x / gif_size.x)
        y_resize: float = (usable.y / gif_size.y)
        return min(x_resize, y_resize)

def _usable_area(default=0.7):
    w = h = 10 ** 10
    for monitor in screeninfo.get_monitors():
        mw, mh = monitor.width, monitor.height
        if mw < w and mh < h:
            w, h = mw, mh
    return Pixels(
        x=int(w * default),
        y=int(h * default)
    )
