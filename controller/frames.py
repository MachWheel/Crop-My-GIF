from concurrent.futures import ThreadPoolExecutor, Future
from io import BytesIO

from PIL import Image
from imageio import v3 as iio

import views
import model

class Frames:
    def __init__(self, gif_info: model.GifInfo):
        loaded = _load_all(gif_info)
        self.loaded = [frame.result() for frame in loaded]


def _load_all(info: model.GifInfo) -> list[Future[bytes]]:
    frames = iio.imiter(info.gif_file)
    with ThreadPoolExecutor() as e:
        i, results = 0, []
        progress = views.PROGRESS(bar_end=info.n_frames)
        for frame in frames:
            progress.read(timeout=10)
            progress['-PROG-'].update(i + 1)
            results.append(e.submit(_load, frame, info))
            i += 1
        progress.close()
    return results

def _load(frame: iio, info: model.GifInfo) -> bytes:
    if info.resize_factor == 1.0:
        return _png_load(frame)
    return _png_resize_load(frame, info)

def _png_load(frame) -> bytes:
    with BytesIO() as output:
        iio.imwrite(output, frame, format_hint='.png')
        return output.getvalue()

def _png_resize_load(frame, info: model.GifInfo) -> bytes:
    frame = Image.fromarray(frame).resize(
        resample=Image.Resampling.LANCZOS,
        reducing_gap=1.0,
        size=info.display_size
    )
    with BytesIO() as output:
        frame.save(output, format='png')
        return output.getvalue()
