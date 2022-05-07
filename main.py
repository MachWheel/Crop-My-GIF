import ctypes
import platform

import PySimpleGUI as sg

from controller import Controller
from model.gif_frames import GifFrames
from model.gif_info import GifInfo


def set_windows_dpi():
    if platform.system() == "Windows":
        if platform.release() == "7":
            ctypes.windll.user32.SetProcessDPIAware()
        elif platform.release() == "8" or platform.release() == "10":
            ctypes.windll.shcore.SetProcessDpiAwareness(1)


def main(info: GifInfo, frames: GifFrames):
    controller = Controller(info, frames)
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
        gif_info = GifInfo(file_name)
        gif_frames = GifFrames(gif_info)
        main(gif_info, gif_frames)
