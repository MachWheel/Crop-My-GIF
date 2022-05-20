from threading import Thread
from time import sleep

from PySimpleGUI import Window

from model.gif_info import GifInfo


class Animation:
    def __init__(self, view: Window, gif_info: GifInfo):
        self._view = view
        self._info = gif_info
        self._stop_animation = False

    def start(self):
        frames_thread = Thread(
            target=self._frame_events,
            args=(
                self._info.n_frames,
                lambda: self._stop_animation,
            ),
            daemon=True
        )
        frames_thread.start()

    def _frame_events(self, n_frames: int, stop):
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
        self._view.hide()
        self._stop_animation = True

    def unhide_and_resume(self):
        self._view.un_hide()
        self._stop_animation = False
        self.start()
