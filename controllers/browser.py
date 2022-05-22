import os

import PySimpleGUI as sg

import views
from . import _icons


class Browser:
    def __init__(self):
        self.view = views.GET_FILE()
        self.browse = self.view['-BROWSE_BTN-']
        self.start = self.view['-START_BTN-']
        self.input = self.view['-FILE_IN-']
        self.file = None

    def get_file(self) -> str | None:
        event, values = self.view.read(timeout=10)

        if event == '-START_BTN-':
            self.view.close()
            return self.file

        if event == sg.WIN_CLOSED:
            self.view.close()
            return 'close'

        if self.input.get() != self.file:
            self.file = self.input.get()
            self.input.set_tooltip(self.input.get())
            valid = self.valid_gif()
            self.change_state(valid)


    def valid_gif(self) -> bool:
        file = self.file
        is_file = (file and os.path.isfile(file))
        is_gif = '.gif' in str(file).lower()
        return is_file and is_gif

    def change_state(self, valid: bool) -> None:
        disabled = False if valid else 'ignore'
        self.start.update(visible=valid)
        self.browse.update(image_data=_icons.FOLDER(disabled))
        self.input.set_size(size=(20 if disabled else 28, None))
