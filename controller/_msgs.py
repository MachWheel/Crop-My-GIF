from random import choice

from model import units


def START_TXT(box: units.CropBox):
    return f"Left:  {box.x0} px\nTop:  {box.y0} px"

def END_TXT(box: units.CropBox):
    return f"Right:  {box.x1} px\nBottom:  {box.y1} px"

def NEW_SIZE_TXT(box: units.CropBox):
    new_w = abs(box.x1 - box.x0 + 1)
    new_h = abs(box.y1 - box.y0 + 1)
    size = units.Pixels(new_w, new_h)
    return f"New size:\n{size.x}x{size.y} px"


def SLOW_EXPORTING() -> str:
    return choice([
        "This might take some time...",
        "Sorry to keep you waiting...",
        "Holy ****! That'px a huge file...",
        "That'px a large GIF you have huh...",
        "Still going...",
        "Almost there...",
    ])
