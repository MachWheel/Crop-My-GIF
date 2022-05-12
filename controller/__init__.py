import PySimpleGUI as sg

import model
from views import CROP_GIF_VIEW, OUTPUT_VIEW
from .animation import Animation
from .crop_info import CropInfo
from .gif_cropper import GifCropper
from .gif_graph import GifGraph


class Controller:
    def __init__(self, info: model.GifInfo, frames: model.GifFrames):
        """
        Initializes a Controller instance
        """
        self.gif_info = info
        self.view = CROP_GIF_VIEW(info.display_size)
        self.info = CropInfo(self.view, info)
        self.graph = GifGraph(self.view, frames)
        self.animation = Animation(self.view, info)
        self.selection = model.units.CropSelection(info.resize_factor)
        self.animation.start()

    def get_cropper(self):
        info = self.gif_info
        box = self.selection.real_box
        preserve_fps = self.info.preserve_fps
        return GifCropper(info, box, preserve_fps)

    def read_events(self) -> str | None:
        """
        Reads window events and returns 'done'
        if the execution finishes.
        """
        event, values = self.view.read(timeout=50)

        if event == sg.WINDOW_CLOSED:
            self.view.close()
            return 'done'

        if event == 'NextFrame':
            index = values.get('NextFrame', 0)
            self.graph.draw_gif_frame(index)
            if self.graph.drawing:
                self.graph.draw_selection(self.selection)

        if (('-GRAPH-' in event) and
                (None not in values['-GRAPH-'])):
            self.selection.update(values['-GRAPH-'])
            self.info.update_info(self.selection.real_box)
            self.graph.draw_selection(self.selection)

        if event == '-CROP_BTN-':
            if self.selection.half_selected:
                return
            self.animation.hide_and_pause()
            cropper = self.get_cropper()
            output = cropper.export_gif()
            OUTPUT_VIEW(output)
            self.animation.unhide_and_resume()

        if event == '-RESET_BTN-':
            self.selection.clear()
            self.info.clear()
