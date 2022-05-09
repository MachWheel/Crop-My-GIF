from os import startfile
from os.path import realpath

import PySimpleGUI as sg

from model.units import Pixels
from views._icons import CLOCK
from . import _frames
from ._labels import (
    MAIN_WINDOW_TITLE, BAR_COLOR, EXPORTING_MSG,
    F_BOLD_12, EXPORTING_WINDOW_TITLE, EXPORTED_MSG,
    IMPORTING_MSG
)


def CROP_GIF_VIEW(img_size: Pixels):
    layout = [
        [sg.Graph(
            canvas_size=(img_size.x, img_size.y),
            graph_bottom_left=(0, img_size.y),
            graph_top_right=(img_size.x, 0),
            key='-GRAPH-',
            enable_events=True,
            background_color='green'
        )],
        [_frames.SELECTION_FRAME(), _frames.CROP_FRAME()],
    ]
    return sg.Window(
        title=MAIN_WINDOW_TITLE,
        layout=layout,
        finalize=True,
        element_justification='center'
    )


def PROGRESS_VIEW(importing=True, bar_end=100):
    txt = IMPORTING_MSG(bar_end) if importing else EXPORTING_MSG
    layout = [
        [sg.Text(txt, key='-TXT-', font=F_BOLD_12)],
        [sg.ProgressBar(
            bar_end,
            orientation='h',
            size=(50, 20),
            key='-PROG-',
            bar_color=BAR_COLOR
        )]
    ]
    return sg.Window(EXPORTING_WINDOW_TITLE, layout)


def OUTPUT_VIEW(output):
    open_file = sg.popup_yes_no(EXPORTED_MSG)
    if open_file == 'Yes':
        startfile(realpath(output))
