import platform
from os.path import isfile
from ctypes import windll

import model
from controller import Controller
from views import GET_FILE_VIEW


def set_windows_dpi():
    if platform.system() == "Windows":
        ver = platform.release()
        if ver == "7":
            windll.user32.SetProcessDPIAware()
        elif ver == ("8" or "10"):
            windll.shcore.SetProcessDpiAwareness(1)


def main(info: model.GifInfo, frames: model.GifFrames):
    controller = Controller(info, frames)
    state = ''
    while state != 'done':
        state = controller.read_events()
    return


if __name__ == "__main__":
    set_windows_dpi()
    file = GET_FILE_VIEW()
    if not file or not isfile(file):
        raise SystemExit('No file selected')
    gif_info = model.GifInfo(file)
    gif_frames = model.GifFrames(gif_info)
    main(gif_info, gif_frames)
