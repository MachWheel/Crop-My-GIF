from model.gif_info import GifInfo
from model.units import CropBox, Pixels


class CropInfo:
    def __init__(self, view, gif_info: GifInfo):
        self._start_txt = view['-START-']
        self._end_txt = view['-END-']
        self._size_txt = view['-BOX-']
        self._btns = (view['-RESET_BTN-'], view['-CROP_BTN-'])
        self._resize = gif_info.resize_factor


    def update(self, box: CropBox):
        box = _fix_inverted_box(box)
        crop = _real_box_size(self._resize, box)
        if (crop.x1 or crop.y1) is not None:
            self._set_all_info(crop)
        self._set_start_info(crop)
        return


    def clear(self):
        self._start_txt.update('None')
        self._end_txt.update('None')
        self._size_txt.update('None')
        self._set_btns_state(disabled=True)


    def _set_start_info(self, box: CropBox):
        self._set_btns_state(disabled=True)
        start_txt = f"{box.x0} px / {box.y0} px"
        self._start_txt.update(start_txt, text_color='yellow')


    def _set_all_info(self, box: CropBox):
        self._set_btns_state(disabled=False)
        start, end, new_size = _format_all_info(box)
        self._start_txt.update(start, text_color='white')
        self._end_txt.update(end)
        self._size_txt.update(new_size)


    def _set_btns_state(self, disabled: bool):
        for btn in self._btns:
            btn.update(disabled=disabled)


def _real_box_size(resize: float, box: CropBox):
    if resize == 1.0:
        return box
    box = [int(n / resize) for n in box if n is not None]
    if len(box) == 4:
        return CropBox(*box)
    return CropBox(box[0], box[1], None, None)


def _format_all_info(box: CropBox) -> tuple[str, str, str]:
    new_w = abs(box.x1 - box.x0 + 1)
    new_h = abs(box.y1 - box.y0 + 1)
    size = Pixels(new_w, new_h)
    start = f"{box.x0} px / {box.y0} px"
    end = f"{box.x1} px / {box.y1} px"
    new_size = f"{size.x}x{size.y} px"
    return start, end, new_size


def _fix_inverted_box(box: CropBox) -> CropBox:
    if box.x0 < box.x1 and box.y0 < box.y1:
        return box
    start = box.x1, box.y1
    end = box.x0, box.y0
    return CropBox(*start, *end)
