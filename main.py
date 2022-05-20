import platform
from os import path
from ctypes import windll

import model
import views
from controller import Controller


def set_windows_dpi():
    if platform.system() == "Windows":
        ver = platform.release()
        if ver == "7":
            windll.user32.SetProcessDPIAware()
        elif ver == ("8" or "10"):
            windll.shcore.SetProcessDpiAwareness(1)


def main(application: Controller):
    state = ''
    while state != 'done':
        state = application.read_events()
    return


if __name__ == "__main__":
    set_windows_dpi()
    file = views.GET_FILE()
    if not file or not path.isfile(file):
        raise SystemExit('No file selected')
    gif_info = model.GifInfo(file)
    controller = Controller(gif_info)
    main(controller)
