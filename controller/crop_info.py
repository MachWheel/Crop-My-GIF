from controller._msgs import START_TXT, END_TXT, NEW_SIZE_TXT
from model.gif_info import GifInfo
from model.units import CropBox


class CropInfo:
    def __init__(self, view, gif_info: GifInfo):
        self._start_txt = view['-START-']
        self._end_txt = view['-END-']
        self._size_txt = view['-BOX-']
        self._reset_btn = view['-RESET_BTN-']
        self._crop_btn = view['-CROP_BTN-']
        self._preserve_check = view['-PRESERVE_CHECK-']
        self._resize = gif_info.resize_factor

    @property
    def preserve_fps(self):
        return self._preserve_check.get()

    def update_info(self, box: CropBox):
        if (box.x1 or box.y1) is not None:
            return self._set_all_info(box)
        return self._set_start_info(box)

    def clear(self):
        txt = 'Click GIF'
        self._start_txt.update(txt, text_color='white')
        self._end_txt.update(txt)
        self._size_txt.update(txt, text_color='white')
        self._set_inputs_state(disabled=True)

    def _set_start_info(self, box: CropBox):
        start_txt = START_TXT(box)
        self._reset_btn.update(disabled=False)
        self._start_txt.update(start_txt, text_color='yellow')

    def _set_all_info(self, box: CropBox):
        self._set_inputs_state(disabled=False)
        self._start_txt.update(START_TXT(box), text_color='white')
        self._end_txt.update(END_TXT(box))
        self._size_txt.update(NEW_SIZE_TXT(box), text_color='yellow')

    def _set_inputs_state(self, disabled: bool):
        self._reset_btn.update(disabled=disabled)
        self._crop_btn.update(disabled=disabled)
        self._preserve_check.update(disabled=disabled)
