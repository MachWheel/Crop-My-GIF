from threading import Thread
from time import sleep

from PySimpleGUI import Window

from model.gif_info import GifInfo


class Animation:
    """
    Controls and generates PySimpleGUI Window
    events related to the currently displayed
    GIF animation.
    """
    def __init__(self, view: Window, gif_info: GifInfo):
        """
        Initializes a new Animation object.

        :param view: PySimpleGUI Window to control
        :type view: sg.Window

        :param gif_info: Object containing the GIF file information
        :type gif_info: model.GifInfo
        """
        self._view = view
        self._info = gif_info
        self._stop_animation = False

    def start(self):
        """
        Starts a thread that generates animation events.
        """
        frames_thread = Thread(
            target=self._frame_events,
            args=(
                self._info.n_frames,
                lambda: self._stop_animation,
            ),
            daemon=True
        )
        frames_thread.start()

    def _frame_events(self, n_frames: int, stop) -> None:
        """
        Needs to be called within a thread.

        Generates a PySimpleGUI Window event tuple:
        ("NextFrame", n) every 0.01 second,

        where "n" is the current gif frame index.

        :param n_frames: Total number of frames
        :type n_frames: int

        :param stop: Returns _stop_animation flag state
        :type stop: () -> bool
        """
        print('Animation thread started.')
        frame = 0
        while True:
            if stop():
                print('Animation thread killed.')
                break
            sleep(0.01)
            frame = (frame + 1) % n_frames
            self._view.write_event_value('NextFrame', frame)

    def hide_and_pause(self):
        """Hides current view and stops the animation thread."""
        self._view.hide()
        self._stop_animation = True

    def unhide_and_resume(self):
        """Shows currently hidden view and restarts the animation thread."""
        self._view.un_hide()
        self._stop_animation = False
        self.start()
