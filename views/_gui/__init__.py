import PySimpleGUI as sg

from model import Pixels
from . import txt, style


def SELECTION_FRAME():
    layout = [[
        sg.T(txt.DEFAULT_INFO, key="-START-", font=style.F_BOLD_10),
        sg.T('to'),
        sg.T(txt.DEFAULT_INFO, key="-END-", font=style.F_BOLD_10),
        sg.Button(
            txt.RESET_BTN,
            key="-RESET_BTN-",
            disabled=True,
            font=style.F_BOLD_10,
            button_color=('white', 'red4'))
    ]]
    return sg.Frame(
        title=txt.SELECT_FRAME,
        layout=layout,
        font=style.F_BOLD_8,
        vertical_alignment='center',
        element_justification='center'
    )


def CROP_FRAME():
    layout = [[
        sg.Text(txt.DEFAULT_INFO, key="-BOX-", font=style.F_BOLD_10),
        sg.Button(
            txt.CROP_BTN,
            key="-CROP_BTN-",
            disabled=True,
            font=style.F_BOLD_10,
            button_color=('white', 'blue4')
        ),
        sg.Checkbox(
            txt.PRESERVE_CHECK,
            default=True,
            disabled=True,
            tooltip=txt.PRESERVE_FPS_TOOLTIP,
            key='-PRESERVE_CHECK-'
        )
    ]]
    return sg.Frame(
        txt.CROP_FRAME, layout=layout,
        font=style.F_BOLD_8,
        vertical_alignment='center',
        element_justification='center'
    )

def GIF_GRAPH(img_size: Pixels):
    return sg.Graph(
            canvas_size=(img_size.x, img_size.y),
            graph_bottom_left=(0, img_size.y),
            graph_top_right=(img_size.x, 0),
            key='-GRAPH-',
            enable_events=True,
            background_color='green'
        )

def PROGRESS_BAR(bar_end):
    return sg.ProgressBar(
            bar_end,
            orientation='h',
            size=(50, 20),
            key='-PROG-',
            bar_color=style.BAR_COLOR
        )
