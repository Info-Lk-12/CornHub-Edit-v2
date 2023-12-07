import threading
from time import sleep

from utils.action_emitter import Emitter


class Editor(Emitter):
    def __init__(self):
        super().__init__()
        self._text = ""
        self.autosave_on = False

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def autosave(self, interval):
        self.autosave_on = True
        while self.autosave_on:
            self.save()
            sleep(interval)

    def start_autosave(self, interval):
        threading.Thread(target=self.autosave, args=(interval,), daemon=True).start()

    def stop_autosave(self):
        self.autosave_on = False
