from concurrent.futures import Future
from random import choice

from views import PROGRESS_VIEW


def TASK_PROGRESS(task: Future[str]):
    bar_end, reload_i, i = 100, 99, 0
    view = PROGRESS_VIEW(importing=False, bar_end=bar_end)
    while task.running():
        view.read(timeout=10)
        if i == reload_i:
            i = 0
            view['-TXT-'].update(_SLOW_EXPORTING())
        view['-PROG-'].update(current_count=(i + 1))
        i += 1
    view.close()


def _SLOW_EXPORTING() -> str:
    return choice([
        "This might take some time...",
        "Sorry to keep you waiting...",
        "Holy ****! That's a huge file...",
        "That's a large GIF you have huh...",
        "Still going...",
        "Almost there...",
    ])
