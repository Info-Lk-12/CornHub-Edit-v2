from tkinter import Menu

from utils.action_emitter import Emitter


class EmitterMenu(Menu):
    def __init__(self, master):
        super().__init__(master, tearoff=False)
        self.emitter = Emitter()

    def add_btn(self, name, label, *args, **kwargs):
        self.add_command(label=label, command=lambda: self._emit(name), *args, **kwargs)

    def _emit(self, event):
        self.emitter._emit(event)

    def on(self, event, callback):
        self.emitter.on(event, callback)


class BasicMenu(Menu):
    def __init__(self, master):
        super().__init__(master, tearoff=False)
        self.listener = None

    def add_btn(self, name, label, *args, **kwargs):
        self.add_command(label=label, command=lambda: self.__call_listener(name), *args, **kwargs)

    def attach_listener(self, listener):
        self.listener = listener

    def __call_listener(self, event):
        if self.listener is not None:
            self.listener(event)


class AppMenu(EmitterMenu):
    def __init__(self, master):
        super().__init__(master)

        file_menu = BasicMenu(self)
        file_menu.attach_listener(self._emit)
        file_menu.add_btn('new', 'New File')
        file_menu.add_btn('open', 'Open')
        file_menu.add_btn('save', 'Save')
        file_menu.add_btn('save_as', 'Save As')
        file_menu.add_btn('exit', 'Exit')

        snippets_menu = BasicMenu(self)
        snippets_menu.attach_listener(self._emit)
        snippets_menu.add_btn('email', 'E-Mail')

        options_menu = BasicMenu(self)
        options_menu.attach_listener(self._emit)
        options_menu.add_btn('enable_autosave', 'Enable Autosave')
        options_menu.add_btn('disable_autosave', 'Disable Autosave')

        self.add_cascade(label="File", menu=file_menu)
        self.add_cascade(label="Snippets", menu=snippets_menu)
        self.add_cascade(label="Options", menu=options_menu)


class ContextMenu(EmitterMenu):
    def __init__(self, master):
        super().__init__(master)

        self.add_btn('cut', 'Cut')
        self.add_btn('copy', 'Copy')
        self.add_btn('paste', 'Paste')
