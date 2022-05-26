"""
Contains the application entry point and startup routine.
"""
import model
import startup
from controllers import App


def main(app: App):
    """
    Reads main application events until its state becomes 'done'

    :param app: Object containing the Application controller
    :type app: controllers.app.App
    """
    state = ''
    while state != 'done':
        state = app.read_events()
    return


if __name__ == "__main__":
    startup.close_splash()
    startup.set_windows_dpi()
    file = startup.browse_gif()
    gif_info = model.GifInfo(file)
    application = App(gif_info)
    main(application)
    