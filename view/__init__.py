import PySimpleGUI as sg

from model.units import Pixels
from view._icons import CLOCK


def LOADING_VIEW(mode: str):
    return sg.popup_no_buttons(
        (f'Please wait:\n'
         f'{mode.capitalize()} GIF...\n\n'
         f'This might take some\n'
         f'time depending on the\n'
         f'size of your file.\n'),
        non_blocking=True,
        font='Default 12 bold',
        no_titlebar=True,
        image=CLOCK
    )


def CROP_VIEW(img_size: Pixels):
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
        sg.Text("Left / Top:"),
        sg.Text("", key="-START-", font=bold),
        sg.Text("to Right / Bottom:"),
        sg.Text("", key="-END-", font=bold),
        sg.Text("New size:"),
        sg.Text("", key="-BOX-", font=bold),
        sg.Button("Reset", key="-RESET_BTN-", disabled=True, p=(5, 10)),
        sg.Button("CROP", key="-CROP_BTN-", disabled=True, p=(5, 10)),
    ]
    return sg.Frame(
        title='Size from:',
        layout=[layout],
        expand_x=True,
        font=underline,
        size=(600, 70)
    )
