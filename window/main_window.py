import platform

from tkinter import Tk, BOTH
from tkinter.scrolledtext import ScrolledText

from editor import Editor
from .main_menu import AppMenu, ContextMenu


class CornHubEditWindow(Tk):
    def __init__(self, editor: Editor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("CornHub Edit")
        self.geometry("960x540")
        self.protocol("WM_DELETE_WINDOW", self._on_close)

        self.text_area = ScrolledText(self, height=35, undo=True)
        self.text_area.pack(fill=BOTH, expand=True)
        self.menu = AppMenu(self)
        self.click_menu = ContextMenu(self.text_area)

        if platform.system() == "Windows":
            self.iconbitmap("assets/logo_win.ico")
        else:
            # self.iconbitmap("assets/logo_unix.png")
            pass

        self.config(menu=self.menu)
        self.editor = editor
        self.attach_listeners()

        editor.on("change", self._on_change)

    def _on_change(self):
        self.text_area.delete(1.0, "end")
        self.text_area.insert(1.0, self.editor.text)

    def _on_close(self):
        self.destroy()


    def attach_listeners(self):
        self.menu.on("exit", self.editor.close_editor)
        self.menu.on("new", self.editor.new_file)
        self.menu.on("open", self.editor.open_file)
        self.menu.on("save", self.editor.save_file)
        self.menu.on("save_as", self.editor.save_as_file)
