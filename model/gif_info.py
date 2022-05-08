from PIL import Image
from screeninfo import get_monitors

from model.units import Pixels


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
        """
        Returns gif current displaying
        size as **Pixels(x, y)**
        """
        width = int(self.size.x * self.resize_factor)
        height = int(self.size.y * self.resize_factor)
        return Pixels(width, height)


def _get_resize_factor(size: Pixels, monitor_area=0.7) -> float:
    """
    Gets the available monitor display
    resolution for the gif object.
    """
    w, h = 100000, 100000
    for mon in get_monitors():
        if mon.width < w and mon.height < h:
            w, h = mon.width, mon.height
    w, h = int(w * monitor_area), int(h * monitor_area)
    area = Pixels(w, h)
    if size.x <= area.x and size.y <= area.y:
        return 1.0
    else:
        x_resize: float = (area.x / size.x)
        y_resize: float = (area.y / size.y)
        return min(x_resize, y_resize)
