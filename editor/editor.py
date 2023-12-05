from utils.action_emitter import Emitter


class Editor(Emitter):
    def __init__(self):
        super().__init__()
        self._text = ""

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
