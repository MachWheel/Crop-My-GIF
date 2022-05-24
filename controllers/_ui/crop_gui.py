from model.gif_info import GifInfo
from model.units import CropBox
from controllers import _msgs


class CropGUI:
    """
    Handles user crop selection UI info and
    controls in a given PySimpleGUI Window.
    """
    def __init__(self, view, gif_info: GifInfo):
        """
        Initializes a new CropGUI object.

        :param view: PySimpleGUI Window to control
        :type view: sg.Window

        :param gif_info: Object containing the GIF file information
        :type gif_info: model.GifInfo
        """
        self._start_txt = view['-START-']
        self._end_txt = view['-END-']
        self._size_txt = view['-BOX-']
        self._reset_btn = view['-RESET_BTN-']
        self._crop_btn = view['-CROP_BTN-']
        self._preserve_check = view['-PRESERVE_CHECK-']
        self._resize = gif_info.resize_factor

    @property
    def preserve_fps(self) -> bool:
        """Returns 'Preserve FPS' control state as a boolean value"""
        return self._preserve_check.get()

    def update_info(self, box: CropBox) -> None:
        """
        Updates crop selection UI information elements
        and changes crop UI controls state according to
        current selection.

        :param box: Selected crop coordinates as
            a named tuple: CropBox(x0, y0, x1, y1)
        :type box: model.units.CropBox
        """
        if (box.x1 or box.y1) is not None:
            return self._set_all_info(box)
        return self._set_start_info(box)

    def clear(self) -> None:
        """
        Clears all crop selection UI information elements
        and disables crop UI controls.
        """
        txt = 'Click GIF'
        self._start_txt.update(txt, text_color='white')
        self._end_txt.update(txt)
        self._size_txt.update(txt, text_color='white')
        self._set_inputs_state(disabled=True)

    def _set_start_info(self, box: CropBox) -> None:
        """
        Updates crop selection start information UI elements
        and enables the 'Clear Selection' button.

        :param box: Selected crop coordinates as
            a named tuple: CropBox(x0, y0, x1, y1)
        :type box: model.units.CropBox
        """
        start_txt = _msgs.START_TXT(box)
        self._reset_btn.update(disabled=False)
        self._start_txt.update(start_txt, text_color='yellow')

    def _set_all_info(self, box: CropBox) -> None:
        """
        Updates all crop selection information UI
        elements and enables all crop UI controls.
        """
        self._set_inputs_state(disabled=False)
        self._start_txt.update(_msgs.START_TXT(box), text_color='white')
        self._end_txt.update(_msgs.END_TXT(box))
        self._size_txt.update(_msgs.NEW_SIZE_TXT(box), text_color='yellow')

    def _set_inputs_state(self, disabled: bool) -> None:
        """
        Enables or disables all crop related UI controls.

        :param disabled: State to change into
        :type disabled: bool
        """
        self._reset_btn.update(disabled=disabled)
        self._crop_btn.update(disabled=disabled)
        self._preserve_check.update(disabled=disabled)
