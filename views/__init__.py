from os import startfile
from os.path import realpath

import PySimpleGUI as sg

from model.units import Pixels
from views._icons import CLOCK
from . import _frames
from ._labels import (
    MAIN_WINDOW_TITLE, BAR_COLOR, EXPORTING_MSG,
    F_BOLD_12, EXPORTING_WINDOW_TITLE, EXPORTED_MSG
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

def LOADING_VIEW(mode: str, current_i, max_i):
    title = f'{mode.capitalize()} {max_i} GIF frames'
    return sg.one_line_progress_meter(
        title=title,
        current_value=current_i + 1,
        max_value=max_i,
        key='-PROG-',
        orientation='h',
        no_button=True,
        keep_on_top=True,
        bar_color=BAR_COLOR,
        size=(38, 8)
    )

def PROGRESS_VIEW(bar_max=100):
    layout = [
        [sg.Text(EXPORTING_MSG, key='-TXT-', font=F_BOLD_12)],
        [sg.ProgressBar(
            bar_max,
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
