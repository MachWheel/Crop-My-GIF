import PySimpleGUI as sg

from views._labels import (
    DEFAULT_INFO_TXT, F_BOLD_10, CROP_BTN_TXT,
    PRESERVE_FPS_TOOLTIP, PRESERVE_CHECK_TXT,
    CROP_FRAME_TXT, F_BOLD_8, RESET_BTN_TXT,
    SELECT_FRAME_TXT
)


def SELECTION_FRAME():
    layout = [[
        sg.T(DEFAULT_INFO_TXT, key="-START-", font=F_BOLD_10),
        sg.T('to'),
        sg.T(DEFAULT_INFO_TXT, key="-END-", font=F_BOLD_10),
        sg.Button(
            RESET_BTN_TXT,
            key="-RESET_BTN-",
            disabled=True,
            font=F_BOLD_10,
            button_color=('white', 'red4'))
    ]]
    return sg.Frame(
        title=SELECT_FRAME_TXT,
        layout=layout,
        font=F_BOLD_8,
        vertical_alignment='center',
        element_justification='center'
    )


def CROP_FRAME():
    layout = [[
        sg.Text(DEFAULT_INFO_TXT, key="-BOX-", font=F_BOLD_10),
        sg.Button(
            CROP_BTN_TXT,
            key="-CROP_BTN-",
            disabled=True,
            font=F_BOLD_10,
            button_color=('white', 'blue4')
        ),
        sg.Checkbox(
            PRESERVE_CHECK_TXT,
            default=True,
            disabled=True,
            tooltip=PRESERVE_FPS_TOOLTIP,
            key='-PRESERVE_CHECK-'
        )
    ]]
    return sg.Frame(
        CROP_FRAME_TXT, layout=layout,
        font=F_BOLD_8,
        vertical_alignment='center',
        element_justification='center'
    )
