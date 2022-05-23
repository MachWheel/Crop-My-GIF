from .units import Pixels, CropBox


class Selection:
    """
    Holds and process information about
    user selected crop area.
    """
    def __init__(self, resize_factor: float):
        """
        Initializes a new Selection object

        :param resize_factor: GIF display
            resize factor as a float value
        :type resize_factor: float
        """
        self.start = _empty_pixels()
        self.end = _empty_pixels()
        self._box = _empty_crop_box()
        self._resize_factor = resize_factor

    @property
    def not_selected(self) -> bool:
        """
        Returns True if there is no selection
        start xy coordinates
        """
        return self.start == _empty_pixels()

    @property
    def half_selected(self) -> bool:
        """
        Returns True if there is no selection
        end xy coordinates
        """
        return self.end == _empty_pixels()

    @property
    def box(self) -> CropBox:
        """
        Returns the selected crop coordinates as
        a named tuple: CropBox(x0, y0, x1, y1)
        """
        resize = self._resize_factor
        box = self._box
        end = box.x1, box.y1
        if resize != 1.0:
            real_px = (_real_size(px, resize) for px in box)
            box = CropBox(*real_px)
        if None in end:
            return box
        return _sorted_box(box)

    def update(self, coordinates: tuple[int, int]) -> None:
        """
        Updates Selection with current selected coordinates.

        :param coordinates: Selected coordinates as a tuple
        :type coordinates: tuple[int, int]
        """
        selected_coordinate = Pixels(*coordinates)
        if self.not_selected:
            self.start = selected_coordinate
            self.end = _empty_pixels()
        else:
            self.end = selected_coordinate
        self._box = CropBox(*self.start, *self.end)

    def clear(self) -> None:
        """
        Clears all Selection object coordinates.
        """
        self.start = _empty_pixels()
        self.end = _empty_pixels()
        self._box = _empty_crop_box()


def _empty_pixels():
    """
    Returns a named tuple Pixels(x, y)
    containing: (None, None)
    """
    return Pixels(None, None)

def _empty_crop_box():
    """
    Returns a named tuple CropBox(x0, y0, x1, y1)
    containing: (None, None, None, None)
    """
    return CropBox(None, None, None, None)

def _real_size(px: int | None, resize_factor: float) -> int | None:
    """
    Returns a coordinate value resized according
    to GIF resize factor.

    :param px: Optional: Coordinate to be resized
    :type px: int | None

    :param resize_factor: GIF display resize factor
    :type resize_factor: float

    :returns: Resized coordinate value if provided.
    :rtype: int | None
    """
    if px is None:
        return None
    return int(px / resize_factor)

def _sorted_box(box: CropBox) -> CropBox:
    """
    Sorts the horizontal and vertical current
    selected crop coordinates in ascending
    order.

    :param box: selected crop coordinates as
        a named tuple: CropBox(x0, y0, x1, y1)
    :type box: model.units.CropBox

    :return: Sorted crop coordinates
    :rtype: model.units.CropBox
    """
    x = sorted((box.x0, box.x1))
    y = sorted((box.y0, box.y1))
    return CropBox(x[0], y[0], x[1], y[1])
