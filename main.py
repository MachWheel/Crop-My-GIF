import ctypes
import platform

import PySimpleGUI as sg

import model
from controller import Controller


def set_windows_dpi():
    if platform.system() == "Windows":
        if platform.release() == "7":
            ctypes.windll.user32.SetProcessDPIAware()
        elif platform.release() == "8" or platform.release() == "10":
            ctypes.windll.shcore.SetProcessDpiAwareness(1)


def main(info: model.GifInfo, frames: model.GifFrames):
    controller = Controller(info, frames)
    state = ''
    while state != 'done':
        state = controller.read_events()
    return

if __name__ == "__main__":
    set_windows_dpi()
    file = None
    while not file:
        file = sg.popup_get_file(
            'Select a GIF to crop',
            'Browse GIF',
            file_types=(('GIF', '*.gif'),)
        )
    gif_info = model.GifInfo(file)
    gif_frames = model.GifFrames(gif_info)
    main(gif_info, gif_frames)
