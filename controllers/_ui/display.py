import PySimpleGUI as sg

import model
from .frames import Frames

class Display:
    """
    Controller responsible for drawing GIF frames
    and user selections.
    """
    def __init__(self, view: sg.Window, gif_frames: Frames):
        """
        Initializes a new Display object.

        :param view: PySimpleGUI Window to control
        :type view: sg.Window

        :param gif_frames: Object containing GIF frames
        :type gif_frames: controllers._ui.Frames
        """
        self.selected = None
        self._graph = view['-GRAPH-']
        self._location = (0, 0)
        self._frames = gif_frames
        self._current_frame = None
        self._colors = ['red', 'white']
        self._current_color = 0
        self.draw_gif_frame(0)
        return

    def draw_gif_frame(self, index: int) -> None:
        """
        Displays a GIF frame according to index value

        :param index: Current frame number
        :type index: int
        """
        self._graph.delete_figure(self._current_frame)
        self._current_frame = self._graph.draw_image(
            data=self._frames.loaded[index],
            location=self._location
        )

    def draw_selection(self, selection: model.Selection) -> None:
        """
        Draws a given user selection over the display

        :param selection: Object that holds user selection
        :type selection: model.Selection
        """
        self._current_color = int(not self._current_color)
        self._graph.delete_figure(self.selected)
        if None in selection.end:
            self._draw_start(selection)
        else:
            self._draw_box(selection)

    def _draw_start(self, selection: model.Selection) -> None:
        """
        Draws a dot over the display representing
        the beginning of user selection.

        :param selection: Object that holds user selection
        :type selection: model.Selection
        """
        self.selected = self._graph.draw_point(
            point=selection.start,
            size=10,
            color=self._colors[self._current_color]
        )

    def _draw_box(self, selection: model.Selection) -> None:
        """
        Draws a box over the display representing
        user selected crop area.

        :param selection: Object that holds user selection
        :type selection: model.Selection
        """
        self.selected = self._graph.draw_rectangle(
            top_left=selection.start,
            bottom_right=selection.end,
            line_color=self._colors[self._current_color],
            line_width=3
        )
