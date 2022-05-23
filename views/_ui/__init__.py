import PySimpleGUI as sg

from model import Pixels
from . import icons, txt, style


def TITLE_HEADING() -> tuple[sg.Image, sg.Text]:
    """Returns 'Crop My GIF' heading UI elements as
    a tuple of PySimpleGUI objects [sg.Image, sg.Text]"""
    img = sg.Image(icons.CROP(), p=((0, 6), (20, 6)))
    heading = sg.Text(
        txt.APP_TITLE,
        font=style.F_BOLD_14,
        p=((0, 10), (20, 3)),
    )
    return img, heading


def FILE_FRAME() -> sg.Frame:
    """Returns GIF browser UI elements as a PySimpleGUI Frame object"""
    BROWSE_BTN = sg.Button(
        button_type=sg.BUTTON_TYPE_BROWSE_FILE,
        file_types=txt.GIF_TYPE,
        image_data=icons.FOLDER(),
        key='-BROWSE_BTN-',
        target='-FILE_IN-',
        tooltip=txt.BROWSE_TOOLTIP,
        **style.PNG_BTN_STYLE()
    )
    FILE_INPUT = sg.Input(
        default_text=txt.FILE_INPUT,
        k='-FILE_IN-',
        size=(30, 4),
        expand_x=True,
        disabled=True,
        font=style.F_ITALIC_12,
        border_width=0,
        disabled_readonly_background_color=style.BG_COLOR,
    )
    START_BTN = sg.Button(
        button_type=sg.BUTTON_TYPE_READ_FORM,
        image_data=icons.PLAY(),
        tooltip=txt.START_TOOLTIP,
        key="-START_BTN-",
        enable_events=True,
        **style.PNG_BTN_STYLE()
    )
    layout = [
        [sg.VPush()],
        [BROWSE_BTN, sg.Push(), FILE_INPUT, sg.Push(),  START_BTN],
        [sg.VPush()]
    ]
    return sg.Frame('', layout, relief=sg.RELIEF_RAISED, p=(5, 10))


def CROP_SELECTION_FRAME() -> sg.Frame:
    """Returns crop selection UI elements as a PySimpleGUI Frame object"""
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


def CROP_CONTROLS_FRAME() -> sg.Frame:
    """Returns crop controls UI elements as a PySimpleGUI Frame object"""
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


def GIF_GRAPH(img_size: Pixels) -> sg.Graph:
    """Returns gif display UI element as a PySimpleGUI Graph object"""
    return sg.Graph(
        canvas_size=(img_size.x, img_size.y),
        graph_bottom_left=(0, img_size.y),
        graph_top_right=(img_size.x, 0),
        key='-GRAPH-',
        enable_events=True,
        background_color='green'
    )


def PROGRESS_BAR(bar_end) -> sg.ProgressBar:
    """Returns progress bar UI element as a PySimpleGUI ProgressBar object"""
    return sg.ProgressBar(
        bar_end,
        orientation='h',
        size=(50, 20),
        key='-PROG-',
        bar_color=style.BAR_COLOR
    )
