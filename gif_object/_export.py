import random
from concurrent.futures import Future

from view import EXPORT_PROGRESS


def export_progress(task: Future[str]):
    bar_max = 100
    prog, txt = 0, 0
    view = EXPORT_PROGRESS()
    while task.running():
        view.read(timeout=10)
        if prog == bar_max - 1:
            prog = 0
            view['-TXT-'].update(_SLOW_EXPORTING())
        view['-PROG-'].update(current_count=(prog + 1))
        prog += 1
    view.close()


def _SLOW_EXPORTING():
    return random.choice([
        "This might take some time...",
        "Sorry to keep you waiting...",
        "Holy ****! That's a huge file...",
        "That's a large GIF you have huh...",
        "Still going...",
        "Almost there...",
    ])