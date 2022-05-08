from collections import namedtuple
from typing import Union

Pixels = namedtuple("Pixels", "x y")
CropBox = namedtuple("CropBox", "x0 y0 x1 y1")

def _empty_pixels():
    return Pixels(None, None)

def _empty_crop_box():
    return CropBox(None, None, None, None)


class CropSelection:
    def __init__(self, resize_factor: float):
        self.start = _empty_pixels()
        self.end = _empty_pixels()
        self.box = _empty_crop_box()
        self._resize_factor = resize_factor

    @property
    def not_slected(self):
        return self.start == _empty_pixels()

    @property
    def half_selected(self):
        return self.end == _empty_pixels()

    @property
    def real_box(self):
        resize = self._resize_factor
        box = self.box
        if resize != 1.0:
            box = CropBox(*[_real_size(n, resize) for n in box])
        return _fix_inverted_box(box)

    def update(self, values):
        values = Pixels(*values)
        if self.not_slected:
            self.start = values
            self.end = _empty_pixels()
        else:
            self.end = values
        self.box = CropBox(*self.start, *self.end)

    def clear(self):
        self.start = _empty_pixels()
        self.end = _empty_pixels()
        self.box = _empty_crop_box()


def _real_size(s: Union[int, None], resize: float) -> Union[int, None]:
    if s is None:
        return None
    return int(s / resize)

def _fix_inverted_box(box: CropBox) -> CropBox:
    if (box.x1 or box.y1) is None:
        return box
    elif box.x0 < box.x1 and box.y0 < box.y1:
        return box
    start = box.x1, box.y1
    end = box.x0, box.y0
    return CropBox(*start, *end)
