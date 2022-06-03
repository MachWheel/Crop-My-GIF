"""
This module holds functions that generates
PySimpleGUI view objects as sg.Window and sg.popup:

    * GET_FILE - File browser Window
    * CROP_GIF - GIF cropping Window
    * PROGRESS - Progress bar Window
    * OUTPUT_READY - Output view popup
    * ERROR - Error view popup
"""
import os

import PySimpleGUI as sg

from model import Pixels
from . import _ui


def GET_FILE() -> sg.Window:
    """Returns file browser view as a PySimpleGUI Window object"""
    layout = [
        [_ui.TITLE_HEADING()],
        [_ui.FILE_FRAME()]
    ]
    return sg.Window(
        title=_ui.txt.APP_TITLE,
        layout=layout,
        finalize=True,
        element_justification='center',
        icon=_ui.icons.LOGO(),
    )


def CROP_GIF(img_size: Pixels) -> sg.Window:
    """Returns GIF cropping view as a PySimpleGUI Window object"""
    layout = [
        [_ui.GIF_GRAPH(img_size)],
        [_ui.CROP_SELECTION_FRAME(), _ui.CROP_CONTROLS_FRAME()],
    ]
    return sg.Window(
        title=_ui.txt.APP_TITLE,
        layout=layout,
        finalize=True,
        element_justification='center',
        icon=_ui.icons.LOGO(),
    )


def PROGRESS(importing=True, bar_end=200) -> sg.Window:
    """
    Returns progress bar view as a PySimpleGUI Window object

    :param importing: Optional: (default=True) set False to exporting
    :type importing: bool

    :param bar_end: Optional: Progress bar end limit value (default=200)
    :type bar_end: int
    """
    title = _ui.txt.PROGRESS_TITLE[importing]
    msg = _ui.txt.PROGRESS_MSG(bar_end if importing else 0)
    layout = [
        [sg.Text(msg, key='-TXT-', font=_ui.style.F_BOLD_12)],
        [_ui.PROGRESS_BAR(bar_end)]
    ]
    return sg.Window(
        title,
        layout,
        icon=_ui.icons.LOGO(),
        no_titlebar=True,
        keep_on_top=True
    )


def OUTPUT_READY(output: str) -> None:
    """
    Displays output view as a PySimpleGUI popup

    :param output: Output GIF file path
    :type output: str
    """
    open_file = sg.popup_yes_no(
        _ui.txt.EXPORTED_MSG,
        font=_ui.style.F_BOLD_14,
        icon=_ui.icons.LOGO(),
        no_titlebar=True,
        keep_on_top=True
    )
    if open_file == 'Yes':
        os.startfile(os.path.realpath(output))


def ERROR(msg: str) -> None:
    """
    Displays error view as a PySimpleGUI popup

    :param msg: Error message string
    :type msg: str
    """
    return sg.popup_error(
        f"\n{msg}\n",
        font=_ui.style.F_BOLD_14,
        no_titlebar=True,
        icon=_ui.icons.LOGO(),
        keep_on_top=True
    )
