import model
import startup
from controller import Controller


def main(application: Controller):
    state = ''
    while state != 'done':
        state = application.read_events()
    return


if __name__ == "__main__":
    startup.close_splash()
    startup.set_windows_dpi()
    file = startup.get_file()
    gif_info = model.GifInfo(file)
    controller = Controller(gif_info)
    main(controller)
    