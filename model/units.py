"""
This module holds named tuples that measure pixel units:

    * Pixels - x and y pixel coordinates as int values
    * CropBox - x0, y0 and x1, y1 pixel coordinates as int values
"""
from collections import namedtuple


Pixels = namedtuple("Pixels", "x y")
CropBox = namedtuple("CropBox", "x0 y0 x1 y1")
