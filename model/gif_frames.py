from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

from PIL import Image
from imageio import v3 as iio

from views import LOADING_VIEW
from .gif_info import GifInfo


class GifFrames:
    def __init__(self, gif_info: GifInfo):
        """
        Loads all gif file frames to **self.loaded**
        based on the **gif_info: GifInfo** object specified.
        """
        frames = iio.imiter(gif_info.gif_file)
        with ThreadPoolExecutor() as e:
            i, results = 0, []
            for frame in frames:
                results.append(e.submit(frame_to_ram, frame, gif_info))
                LOADING_VIEW('loading', i, gif_info.n_frames)
                i += 1
        self.loaded = [data.result() for data in results]


def frame_to_ram(frame: iio, gif_info: GifInfo) -> bytes:
    """
    Resizes a gif frame if necessary
    and loads it into memory, returning
    it's contents as *bytes*.
    """
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
