import PySimpleGUI as sg

import model
import views
from . import _ui, _msgs


class Application:
    def __init__(self, gif_info: model.GifInfo):
        """
        Initializes a Application instance
        """
        gif_frames = _ui.Frames(gif_info)
        self.gif_info = gif_info
        self.view = views.CROP_GIF(gif_info.display_size)
        self.gui = _ui.CropGUI(self.view, gif_info)
        self.display = _ui.Display(self.view, gif_frames)
        self.animation = _ui.Animation(self.view, gif_info)
        self.selection = model.Selection(gif_info.resize_factor)
        self.animation.start()

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
            self.display.draw_gif_frame(index)
            if self.display.selected:
                self.display.draw_selection(self.selection)

        if (('-GRAPH-' in event) and
                (None not in values['-GRAPH-'])):
            self.selection.update(values['-GRAPH-'])
            self.gui.update_info(self.selection.real_box)
            self.display.draw_selection(self.selection)

        if event == '-CROP_BTN-':
            if self.selection.half_selected:
                return
            self.animation.hide_and_pause()
            output = self._cropper.export_gif()
            self._show_output(output)
            self.animation.unhide_and_resume()

        if event == '-RESET_BTN-':
            self.selection.clear()
            self.gui.clear()

    @property
    def _cropper(self):
        info = self.gif_info
        box = self.selection.real_box
        preserve_fps = self.gui.preserve_fps
        return _ui.Cropper(info, box, preserve_fps)

    @staticmethod
    def _show_output(output):
        if output:
            views.OUTPUT_READY(output)
            return
        views.ERROR(_msgs.ERROR_MSG)