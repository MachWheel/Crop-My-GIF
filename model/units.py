from collections import namedtuple


Pixels = namedtuple("Pixels", "x y")
CropBox = namedtuple("CropBox", "x0 y0 x1 y1")

def _empty_pixels():
    return Pixels(None, None)

def _empty_crop_box():
    return CropBox(None, None, None, None)


class CropSelection:
    def __init__(self):
        self.start = _empty_pixels()
        self.end = _empty_pixels()
        self.box = _empty_crop_box()

    @property
    def no_selection(self):
        return self.start == _empty_pixels()

    @property
    def still_selecting(self):
        return self.end == _empty_pixels()

    @property
    def is_empty(self):
        return self.box == _empty_crop_box()

    def update(self, values):
        values = Pixels(*values)
        if self.no_selection:
            self.start = values
            self.end = _empty_pixels()
        else:
            self.end = values
        self.box = CropBox(*self.start, *self.end)

    def clear(self):
        self.start = _empty_pixels()
        self.end = _empty_pixels()
        self.box = _empty_crop_box()
