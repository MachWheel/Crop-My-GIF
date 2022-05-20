import model
from .frames import Frames

class Display:
    def __init__(self, view, gif_frames: Frames):
        self.selected = None
        self._graph = view['-GRAPH-']
        self._location = (0, 0)
        self._frames = gif_frames
        self._current_frame = None
        self._colors = ['red', 'white']
        self._current_color = 0
        self.draw_gif_frame(0)
        return

    def draw_gif_frame(self, index):
        self._graph.delete_figure(self._current_frame)
        self._current_frame = self._graph.draw_image(
            data=self._frames.loaded[index],
            location=self._location
        )

    def draw_selection(self, selection: model.Selection):
        self._current_color = int(not self._current_color)
        self._graph.delete_figure(self.selected)
        if None in selection.end:
            self._draw_start(selection)
        else:
            self._draw_box(selection)

    def _draw_start(self, selection):
        self.selected = self._graph.draw_point(
            point=selection.start,
            size=10,
            color=self._colors[self._current_color]
        )

    def _draw_box(self, selection):
        self.selected = self._graph.draw_rectangle(
            top_left=selection.start,
            bottom_right=selection.end,
            line_color=self._colors[self._current_color],
            line_width=3
        )
