import importlib.util
import platform
from ctypes import windll
import os

import views

def close_splash():
    if '_PYIBoot_SPLASH' in os.environ:
        if not importlib.util.find_spec("pyi_splash"):
            return
        import pyi_splash
        pyi_splash.close()

def set_windows_dpi():
    if platform.system() == "Windows":
        ver = platform.release()
        if ver == "7":
            windll.user32.SetProcessDPIAware()
        elif ver == ("8" or "10"):
            windll.shcore.SetProcessDpiAwareness(1)

def get_file() -> str | None:
    file = views.GET_FILE()
    if not file:
        raise SystemExit()
    if not os.path.isfile(file):
        views.ERROR('Please select a valid GIF file.')
        return None
    return file
