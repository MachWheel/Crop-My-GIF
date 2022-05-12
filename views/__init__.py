from os import startfile
from os.path import realpath

import PySimpleGUI as sg

from model.units import Pixels
from ._gui import SELECTION_FRAME, CROP_FRAME, txt, style


def GET_FILE_VIEW():
    return sg.popup_get_file(
        message=txt.SELECT_FILE,
        title=txt.APP_TITLE,
        file_types=(txt.GIF_EXTENSION,)
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
        [SELECTION_FRAME(), CROP_FRAME()],
    ]
    return sg.Window(
        title=txt.APP_TITLE,
        layout=layout,
        finalize=True,
        element_justification='center'
    )


def PROGRESS_VIEW(importing=True, bar_end=100):
    display = txt.IMPORTING_MSG(bar_end) if importing else txt.EXPORTING_MSG
    layout = [
        [sg.Text(display, key='-TXT-', font=style.F_BOLD_12)],
        [sg.ProgressBar(
            bar_end,
            orientation='h',
            size=(50, 20),
            key='-PROG-',
            bar_color=style.BAR_COLOR
        )]
    ]
    return sg.Window(txt.EXPORTING_TITLE, layout)


def OUTPUT_VIEW(output):
    open_file = sg.popup_yes_no(txt.EXPORTED_MSG)
    if open_file == 'Yes':
        startfile(realpath(output))
