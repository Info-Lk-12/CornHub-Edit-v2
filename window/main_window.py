import platform

from tkinter import Tk, BOTH
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename

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

    def open(self):
        self.editor.open_file(askopenfilename())

    def save(self, save_as=False):
        if not save_as and self.editor.path is not None and self.editor.path != "":
            self.editor.save_file()
        else:
            self.editor.save_as_file(asksaveasfilename())

    def attach_listeners(self):
        self.menu.on("new", self.editor.new_file)
        self.menu.on("open", self.open)
        self.menu.on("save", self.save)
        self.menu.on("save_as", lambda: self.save(True))
        self.menu.on("exit", self.editor.close_editor)
