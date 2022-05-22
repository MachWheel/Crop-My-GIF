import importlib.util
import platform
from ctypes import windll
import os

from controllers import GifBrowser

def close_splash():
    """
    Closes the application loading splash screen.
    """
    if '_PYIBoot_SPLASH' in os.environ:
        if not importlib.util.find_spec("pyi_splash"):
            return
        import pyi_splash
        pyi_splash.close()

def set_windows_dpi():
    """
    Sets the application DPI for Windows systems
    """
    if platform.system() == "Windows":
        ver = platform.release()
        if ver == "7":
            windll.user32.SetProcessDPIAware()
        elif ver == ("8" or "10"):
            windll.shcore.SetProcessDpiAwareness(1)

def browse_gif() -> str:
    """
    Displays a popup window asking for user to browse
    and input a GIF file.

    :raise SystemExit: if user closes the window
    :return: The user selected GIF file path
    :rtype: str
    """
    browser, file = GifBrowser(), None
    while not file:
        file = browser.get_file()
    if file == 'close':
        raise SystemExit()
    return file
