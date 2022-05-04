from os import startfile
from os.path import realpath
from threading import Thread
from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

import PySimpleGUI as sg

from model.gif_object import GifObject
from model.units import CropSelection, Pixels
from view import LOADING_VIEW, CROP_VIEW
from .crop_info import CropInfo
from .gif_graph import GifGraph


class Controller:
    def __init__(self, gif_file):
        t_start = perf_counter()
        self.view = LOADING_VIEW('Loading')
        self.gif_obj = GifObject(gif_file)
        self.view = CROP_VIEW(self.gif_obj.display_size)
        self.gif_graph = GifGraph(self.view, self.gif_obj)
        self.crop_info = CropInfo(self.view, self.gif_obj)
        self.selection = CropSelection()
        self.stop_animation = False
        self._start_gif_thread()
        print(f"Loaded in {(perf_counter() - t_start):.2f}s")


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

        if '-GRAPH-' in event and None not in values['-GRAPH-']:
            self.selection.update(values['-GRAPH-'])
            self.crop_info.update(self.selection.box)
            self.gif_graph.draw_selection(self.selection)

        if event == '-CROP_BTN-':
            self.stop_animation = True
            if self.selection.end is Pixels(None, None):
                return
            LOADING_VIEW('Exporting')
            self.view.close()
            with ThreadPoolExecutor() as e:
                task = e.submit(self.gif_obj.crop_gif, self.selection.box)
                output = task.result()
            if output:
                startfile(realpath(output))
            return 'done'

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
