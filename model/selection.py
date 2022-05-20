from .units import Pixels, CropBox


class Selection:
    def __init__(self, resize_factor: float):
        self.start = _empty_pixels()
        self.end = _empty_pixels()
        self.box = _empty_crop_box()
        self._resize_factor = resize_factor

    @property
    def not_selected(self):
        return self.start == _empty_pixels()

    @property
    def half_selected(self):
        return self.end == _empty_pixels()

    @property
    def real_box(self):
        resize = self._resize_factor
        box = self.box
        if resize != 1.0:
            real_px = (_real_size(px, resize) for px in box)
            box = CropBox(*real_px)
        end = box.x1, box.y1
        if None in end:
            return box
        return _sorted_box(box)

    def update(self, values):
        values = Pixels(*values)
        if self.not_selected:
            self.start = values
            self.end = _empty_pixels()
        else:
            self.end = values
        self.box = CropBox(*self.start, *self.end)

    def clear(self):
        self.start = _empty_pixels()
        self.end = _empty_pixels()
        self.box = _empty_crop_box()


def _empty_pixels():
    return Pixels(None, None)

def _empty_crop_box():
    return CropBox(None, None, None, None)

def _real_size(px: int | None, resize: float) -> int | None:
    if px is None:
        return None
    return int(px / resize)

def _sorted_box(box):
    x = sorted((box.x0, box.x1))
    y = sorted((box.y0, box.y1))
    return CropBox(x[0], y[0], x[1], y[1])
