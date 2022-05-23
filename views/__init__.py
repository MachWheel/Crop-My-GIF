from os import startfile
from os.path import realpath

import PySimpleGUI as sg

from model import Pixels
from . import _gui

def GET_FILE() -> sg.Window:
    """Returns file browser view as a PySimpleGUI Window object"""
    layout = [
        [_gui.TITLE_HEADING()],
        [_gui.FILE_FRAME()]
    ]
    return sg.Window(
        title=_gui.txt.APP_TITLE,
        layout=layout,
        finalize=True,
        element_justification='center'
    )

def CROP_GIF(img_size: Pixels) -> sg.Window:
    """Returns GIF cropping view as a PySimpleGUI Window object"""
    layout = [
        [_gui.GIF_GRAPH(img_size)],
        [_gui.SELECTION_FRAME(), _gui.CROP_FRAME()],
    ]
    return sg.Window(
        title=_gui.txt.APP_TITLE,
        layout=layout,
        finalize=True,
        element_justification='center'
    )


def PROGRESS(importing=True, bar_end=200) -> sg.Window:
    """Returns progress bar view as a PySimpleGUI Window object"""
    title = _gui.txt.PROGRESS_TITLE[importing]
    msg = _gui.txt.PROGRESS_MSG(bar_end if importing else 0)
    layout = [
        [sg.Text(msg, key='-TXT-', font=_gui.style.F_BOLD_12)],
        [_gui.PROGRESS_BAR(bar_end)]
    ]
    return sg.Window(title, layout)


def OUTPUT_READY(output) -> None:
    """Displays output view as a PySimpleGUI popup"""
    open_file = sg.popup_yes_no(_gui.txt.EXPORTED_MSG)
    if open_file == 'Yes':
        startfile(realpath(output))


def ERROR(msg):
    """Displays error view as a PySimpleGUI popup"""
    return sg.popup_error(
        f"\n{msg}\n",
        font=_gui.style.F_14,
        no_titlebar=True
    )
