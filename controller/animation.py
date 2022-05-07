from threading import Thread
from time import sleep

from PySimpleGUI import Window

from model.gif_info import GifInfo


class Animation:
    def __init__(self, view: Window, gif_info: GifInfo):
        self.view = view
        self.info = gif_info
        self.stop_animation = False

    def start(self):
        """
        Starts a thread that generates an
        event ('NextFrame', n) every 0.01
        second, where 'n' is the current
        gif frame.
        """
        frames_thread = Thread(
            target=self._frame_events,
            args=(
                self.info.n_frames,
                lambda: self.stop_animation,
            ),
            daemon=True
        )
        frames_thread.start()

    def _frame_events(self, n_frames: int, stop):
        """
        Needs to be called within a thread.
        Generates an event **('NextFrame', n)**
        every **0.01 second**, where '**n**' is the
        **current gif frame**.
        """
        print('Animation thread started.')
        frame = 0
        while True:
            if stop():
                print('Animation thread killed.')
                break
            sleep(0.01)
            frame = (frame + 1) % n_frames
            self.view.write_event_value('NextFrame', frame)

    def hide_and_pause(self):
        self.view.hide()
        self.stop_animation = True

    def unhide_and_resume(self):
        self.view.un_hide()
        self.stop_animation = False
        self.start()
