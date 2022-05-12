from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

from PIL import Image
from imageio import v3 as iio

from views import PROGRESS_VIEW
from .gif_info import GifInfo


class GifFrames:
    def __init__(self, gif_info: GifInfo):
        frames = _frame_loader(gif_info)
        self.loaded = [data.result() for data in frames]


def _frame_loader(info: GifInfo):
    frames = iio.imiter(info.gif_file)
    with ThreadPoolExecutor() as e:
        i, results = 0, []
        loading = PROGRESS_VIEW(bar_end=info.n_frames)
        for frame in frames:
            loading.read(timeout=10)
            loading['-PROG-'].update(i + 1)
            results.append(e.submit(_load_frame, frame, info))
            i += 1
        loading.close()
    return results


def _load_frame(frame: iio, gif_info: GifInfo) -> bytes:
    if gif_info.resize_factor == 1.0:
        with BytesIO() as output:
            iio.imwrite(output, frame, format_hint='.png')
            return output.getvalue()
    else:
        frame = Image.fromarray(frame)
        frame = frame.resize(
            resample=Image.Resampling.LANCZOS,
            reducing_gap=1.0,
            size=gif_info.display_size
        )
        with BytesIO() as output:
            frame.save(output, format='png')
            return output.getvalue()
