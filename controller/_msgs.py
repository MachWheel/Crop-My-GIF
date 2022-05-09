from model.units import CropBox, Pixels


def START_TXT(box: CropBox):
    return f"Left:  {box.x0} px\nTop:  {box.y0} px"

def END_TXT(box: CropBox):
    return f"Right:  {box.x1} px\nBottom:  {box.y1} px"

def NEW_SIZE_TXT(box: CropBox):
    new_w = abs(box.x1 - box.x0 + 1)
    new_h = abs(box.y1 - box.y0 + 1)
    size = Pixels(new_w, new_h)
    return f"New size:\n{size.x}x{size.y} px"