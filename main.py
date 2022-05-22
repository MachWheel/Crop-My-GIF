import model
import startup
from controllers import Application


def main(app: Application):
    state = ''
    while state != 'done':
        state = app.read_events()
    return


if __name__ == "__main__":
    startup.close_splash()
    startup.set_windows_dpi()
    file = startup.get_file()
    gif_info = model.GifInfo(file)
    application = Application(gif_info)
    main(application)
    