from collections import namedtuple

Pixels = namedtuple("Pixels", "x y")
CropBox = namedtuple("CropBox", "x0 y0 x1 y1")


class CropSelection:
    def __init__(self):
        self.start = Pixels(None, None)
        self.end = Pixels(None, None)
        self.box = CropBox(None, None, None, None)

    @property
    def still_selecting(self):
        return self.end == Pixels(None, None)

    @property
    def is_empty(self):
        return self.box == CropBox(None, None, None, None)

    def update(self, values):
        if self.start == (None, None):
            self.start = Pixels(*values)
            self.end = Pixels(None, None)
        else:
            self.end = Pixels(*values)
        self.box = CropBox(*self.start, *self.end)

    def clear(self):
        self.start = Pixels(None, None)
        self.end = Pixels(None, None)
        self.box = CropBox(None, None, None, None)
