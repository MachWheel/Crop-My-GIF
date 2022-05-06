from concurrent.futures import Future
from os import startfile
from os.path import realpath

import PySimpleGUI as sg

from model.units import Pixels
from view._icons import CLOCK


def CROP_GIF(img_size: Pixels):
    layout = [
        [sg.Graph(
            canvas_size=(img_size.x, img_size.y),
            graph_bottom_left=(0, img_size.y),
            graph_top_right=(img_size.x, 0),
            key='-GRAPH-',
            enable_events=True,
            background_color='green'
        )],
        [_CROP_INFO_FRAME()],
    ]
    return sg.Window("Crop GIF", layout, finalize=True, element_justification='center')


def _CROP_INFO_FRAME():
    bold = "Default 10 bold"
    underline = "Default 10 bold underline"
    layout = [
        sg.Frame("Left / Top:", [[
            sg.Text("", key="-START-", font=bold)
        ]]),
        sg.T('to'),
        sg.Frame("Right / Bottom:", [[
            sg.Text("", key="-END-", font=bold)
        ]]),
        sg.Button(
            "Clear Selection", key="-RESET_BTN-", disabled=True,
            font=bold, button_color=('white', 'red4')),
        sg.Frame("New size:", [[
            sg.Text("", key="-BOX-", font=bold, text_color='blue')
        ]]),
        sg.Button(
            "CROP", key="-CROP_BTN-", disabled=True,
            font=bold, button_color=('white', 'blue4')
        ),
    ]
    return sg.Frame(
        title='SIZE FROM:',
        layout=[layout],
        expand_x=True,
        font=underline,
        size=(600, 70)
    )


def LOADING(mode: str, current_i, max_i):
    return sg.one_line_progress_meter(
        title=f'{mode.capitalize()} {max_i} GIF frames',
        current_value=current_i + 1,
        max_value=max_i,
        key='-PROG-',
        orientation='h',
        no_button=True,
        keep_on_top=True,
        bar_color='#d97ff0',
        size=(38, 8)
    )


def EXPORT_PROGRESS(task: Future[str], max_i: int):
    i = 0
    while task.running():
        i += 1
        LOADING('processing', i, max_i)
        if i < max_i - 1:
            continue
        i = 0
    sg.one_line_progress_meter_cancel(key='-PROG-')


def OUTPUT_FILE(output):
    open_file = sg.popup_yes_no(
        'Cropped GIF exported!\n'
        'Would you like to open it?'
    )
    if open_file == 'Yes':
        startfile(realpath(output))
