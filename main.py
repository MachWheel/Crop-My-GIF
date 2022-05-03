import ctypes
import platform

import PySimpleGUI as sg

from controller import Controller


def set_windows_dpi():
    if platform.system() == "Windows":
        if platform.release() == "7":
            ctypes.windll.user32.SetProcessDPIAware()
        elif platform.release() == "8" or platform.release() == "10":
            ctypes.windll.shcore.SetProcessDpiAwareness(1)

def main(file):
    controller = Controller(file)
    while True:
        state = controller.read_events()
        if state == 'done':
            break

if __name__ == "__main__":
    set_windows_dpi()
    file_name = sg.popup_get_file(
        'Select a GIF to crop',
        'Browse GIF',
        file_types=(('GIF', '*.gif'),)
    )
    if file_name:
        main(file_name)
