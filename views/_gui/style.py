import PySimpleGUI as sg

sg.theme('DarkBlue')

BAR_COLOR = '#ff009b'
F_BOLD_8 = 'Default 8 bold'
F_BOLD_10 = 'Default 10 bold'
F_BOLD_12 = 'Default 12 bold'
F_14 = 'Default 14'
F_ITALIC_12 = 'Default 12 italic'
F_BOLD_14 = 'Default 14 bold'
BG_COLOR = sg.theme_background_color()

def PNG_BTN_STYLE() -> dict:
    return {
        "button_color": (BG_COLOR, BG_COLOR),
        "border_width": 0
    }
