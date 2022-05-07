from threading import Thread
from time import sleep

import PySimpleGUI as sg

from gif_object import GifObject
from model.units import CropSelection
from view import CROP_GIF, OUTPUT_FILE
from .crop_info import CropInfo
from .gif_graph import GifGraph


class Controller:
    def _get_view(self):
        return CROP_GIF(self.gif_obj.display_size)

    def _get_graph(self):
        return GifGraph(self.view, self.gif_obj)

    def _get_info(self):
        return CropInfo(self.view, self.gif_obj)

    def __init__(self, gif_file):
        """
        Initializes a Controller instance

        """
        self.gif_obj = GifObject(gif_file)
        self.view = self._get_view()
        self.gif_graph = self._get_graph()
        self.crop_info = self._get_info()
        self.selection = CropSelection()
        self.stop_animation = False
        self._start_gif_thread()

    def read_events(self) -> str | None:
        """
        Reads window events and returns 'done'
        if the execution finishes. \n
        """
        event, values = self.view.read(timeout=50)

        if event == sg.WINDOW_CLOSED:
            return 'done'

        if event == 'NextFrame':
            index = values.get('NextFrame', 0)
            self.gif_graph.animate(index)
            if self.gif_graph.drawing:
                self.gif_graph.draw_selection(self.selection)

        if ('-GRAPH-' in event) and (None not in values['-GRAPH-']):
            self.selection.update(values['-GRAPH-'])
            self.crop_info.update(self.selection.box)
            self.gif_graph.draw_selection(self.selection)

        if event == '-CROP_BTN-':
            if self.selection.still_selecting:
                return
            self._hide_and_pause()
            crop_box = self.selection.box
            output = self.gif_obj.crop_export(crop_box)
            OUTPUT_FILE(output)
            self._unhide_and_play()

        if event == '-RESET_BTN-':
            self.selection.clear()
            self.crop_info.clear()


    def _start_gif_thread(self):
        """
        Starts a thread that generates an
        event ('NextFrame', n) every 0.01
        second, where 'n' is the current
        gif frame.
        """
        thread = Thread(
            target=self._frame_events,
            args=(
                self.gif_obj.n_frames,
                lambda: self.stop_animation,
            ),
            daemon=True
        )
        thread.start()

    def _frame_events(self, n_frames: int, stop):
        """
        Needs to be called withing a thread.\n
        Generates an event ('NextFrame', n) \n
        every 0.01 second, where 'n' is the \n
        current gif frame.
        """
        frame = 0
        while True:
            if stop():
                print('thread killed')
                break
            sleep(0.01)
            frame = (frame + 1) % n_frames
            self.view.write_event_value('NextFrame', frame)

    def _hide_and_pause(self):
        self.view.hide()
        self.stop_animation = True

    def _unhide_and_play(self):
        self.view.un_hide()
        self.stop_animation = False
        self._start_gif_thread()
