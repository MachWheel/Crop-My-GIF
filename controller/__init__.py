import PySimpleGUI as sg

from model.gif_cropper import GifCropper
from model.gif_frames import GifFrames
from model.gif_info import GifInfo
from model.units import CropSelection
from views import CROP_GIF_VIEW, OUTPUT_VIEW
from .animation import Animation
from .crop_info import CropInfo
from .gif_graph import GifGraph


class Controller:
    def __init__(self, info: GifInfo, frames: GifFrames):
        """
        Initializes a Controller instance
        """
        self.gif_info = info
        self.view = CROP_GIF_VIEW(info.display_size)
        self.crop_info = CropInfo(self.view, info)
        self.gif_graph = GifGraph(self.view, frames)
        self.animation = Animation(self.view, info)
        self.selection = CropSelection(info.resize_factor)
        self.animation.start()

    def read_events(self) -> str | None:
        """
        Reads window events and returns 'done'
        if the execution finishes.
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
            print(self.selection.real_box)
            self.gif_graph.draw_selection(self.selection)

        if event == '-CROP_BTN-':
            if self.selection.half_selected:
                return
            self.animation.hide_and_pause()
            crop_box = self.selection.box
            cropper = GifCropper(self.gif_info, crop_box)
            output = cropper.export_gif()
            OUTPUT_VIEW(output)
            self.animation.unhide_and_resume()

        if event == '-RESET_BTN-':
            self.selection.clear()
            self.crop_info.clear()
