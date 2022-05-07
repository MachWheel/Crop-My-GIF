from PIL import Image
from screeninfo import get_monitors

from model.units import Pixels


class GifInfo:
    def __init__(self, file):
        _gif_img = Image.open(file)
        _screen = _get_monitor_area()
        self.gif_file = file
        self.size = Pixels(*_gif_img.size)
        self.n_frames: int = _gif_img.n_frames
        if self.size.x <= _screen.x and self.size.y <= _screen.y:
            self.resize_factor = 1.0
        else:
            factor_x: float = (_screen.x / self.size.x)
            factor_y: float = (_screen.y / self.size.y)
            self.resize_factor = min(factor_x, factor_y)

    @property
    def display_size(self) -> Pixels:
        """
        Returns gif current displaying
        size as **Pixels(x, y)**
        """
        width = int(self.size.x * self.resize_factor)
        height = int(self.size.y * self.resize_factor)
        return Pixels(width, height)


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
