from model.gif_info import GifInfo
from model.units import CropBox, Pixels


class CropInfo:
    def __init__(self, view, gif_info: GifInfo):
        self._start = view['-START-']
        self._end = view['-END-']
        self._size = view['-BOX-']
        self._reset_btn = view['-RESET_BTN-']
        self._crop_btn = view['-CROP_BTN-']
        self._gif_size = gif_info.size
        self._resize_factor = gif_info.resize_factor

    def update(self, crop_box: CropBox):
        crop = self._real_box_size(crop_box)
        if (crop.x1 or crop.y1) is None:
            self._update_start(crop)
            return
        if crop.x0 > crop.x1 and crop.y0 > crop.y1:
            crop = _invert_xy(crop)
        self._update_end(crop)

    def clear(self):
        self._start.update('None')
        self._end.update('None')
        self._size.update('None')
        self._update_btns(disabled=True)


    def _update_start(self, box: CropBox):
        self._start.update(
            f"{box.x0} / {box.y0}",
            text_color='yellow'
        )
        self._update_btns(disabled=True)

    def _update_end(self, box: CropBox):
        size = _crop_size(box)
        self._start.update(f"{box.x0} / {box.y0}",
                           text_color='white')
        self._end.update(f"{box.x1} / {box.y1}")
        self._size.update(f"{size.x}x{size.y} px")
        self._update_btns(disabled=False)

    def _update_btns(self, disabled: bool):
        self._reset_btn.update(disabled=disabled)
        self._crop_btn.update(disabled=disabled)

    def _real_box_size(self, box: CropBox):
        box = [int(n / self._resize_factor)
                for n in box if n is not None]
        if len(box) == 2:
            return CropBox(box[0], box[1], None, None)
        return CropBox(*box)


def _invert_xy(crop: CropBox) -> CropBox:
    start = crop.x1, crop.y1
    end = crop.x0, crop.y0
    return CropBox(*start, *end)

def _crop_size(crop: CropBox) -> Pixels:
    width = abs(crop.x1 - crop.x0 + 1)
    height = abs(crop.y1 - crop.y0 + 1)
    return Pixels(width, height)
