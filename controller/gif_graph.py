from model.gif_object import GifObject
from model.units import CropSelection


class GifGraph:
    def __init__(self, view, gif: GifObject):
        self.graph = view['-GRAPH-']
        self.location = (0, 0)
        self.gif_display = gif
        self.drawing = None
        self.current_frame = None
        self.colors = ['red', 'white']
        self.current_color = 0
        self.animate(0)
        return


    def animate(self, index):
        self.graph.delete_figure(self.current_frame)
        self.current_frame = self.graph.draw_image(
            data=self.gif_display.frames[index],
            location=self.location
        )


    def draw_selection(self, selection: CropSelection):
        self.current_color = int(not self.current_color)
        self.graph.delete_figure(self.drawing)
        if None in selection.end:
            self._draw_start(selection)
        else:
            self._draw_box(selection)


    def _draw_start(self, selection):
        self.drawing = self.graph.draw_point(
            point=selection.start,
            size=10,
            color=self.colors[self.current_color]
        )


    def _draw_box(self, selection):
        self.drawing = self.graph.draw_rectangle(
            top_left=selection.start,
            bottom_right=selection.end,
            line_color=self.colors[self.current_color],
            line_width=3
        )
