from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

from PIL import Image
from imageio import v3 as iio

import model
import views


class Frames:
    def __init__(self, gif_info: model.GifInfo):
        self.loaded = _load_all(gif_info)


def _load_all(info: model.GifInfo) -> list[bytes]:
    frames = iio.imiter(info.gif_file)
    prog = views.PROGRESS(bar_end=info.n_frames)
    i, results, key = 0, [], '-PROG-'
    with ThreadPoolExecutor() as e:
        for frame in frames:
            prog.read(timeout=10)
            prog[key].update(i + 1)
            results.append(e.submit(_load, frame, info))
            i += 1
        prog.close()
    return [frame.result() for frame in results]


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
