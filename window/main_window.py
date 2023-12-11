import platform

from tkinter import Tk, BOTH, END
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

    def _update(self):
        self.editor.text = self.text_area.get(1.0, "end")

    def open(self):
        file_path = askopenfilename()
        if file_path is not None and file_path != "":
            self.editor.open_file(file_path)

    def save(self, save_as=False):
        self._update()
        if not save_as and self.editor.path is not None and self.editor.path != "":
            self.editor.save_file()
        else:
            file_path = asksaveasfilename()
            if file_path is not None and file_path != "":
                self.editor.save_as_file(file_path)

    def select_all(self, *e):
        self.text_area.tag_add("sel", "1.0", "end")
        self.text_area.mark_set("insert", "1.0")
        self.text_area.see("insert")

    def cut(self, *e):
        text = self.text_area.selection_get()

        start = self.text_area.index('sel.first')
        end = self.text_area.index('sel.last')

        self.text_area.delete(start, end)

        self.clipboard_clear()
        self.clipboard_append(text)
        self._update()

    def copy(self, *e):
        text = self.text_area.selection_get()
        self.clipboard_clear()
        self.clipboard_append(text)

    def paste(self, *e):
        text = self.clipboard_get()
        if self.text_area.tag_ranges("sel"):
            start = self.text_area.index('sel.first')
            end = self.text_area.index('sel.last')
            self.text_area.delete(start, end)
        self.text_area.insert(END, text)
        self._update()

    def attach_listeners(self):
        self.text_area.bind('<Button-3>', self.context_menu)

        self.bind("<Control-n>", self.editor.new_file)
        self.bind("<Control-o>", self.open)
        self.bind('<Control-s>', lambda e: self.save())
        self.bind("<Control-Shift-s>", lambda e: self.save(True))
        self.bind("<Alt-F4>", self.quit)

        self.bind("<Control-x>", self.cut)
        self.bind("<Control-c>", self.copy)
        self.bind("<Control-v>", self.paste)

        self.click_menu.on("cut", self.cut)
        self.click_menu.on("copy", self.copy)
        self.click_menu.on("paste", self.paste)

        self.menu.on("new", self.editor.new_file)
        self.menu.on("open", self.open)
        self.menu.on("save", self.save)
        self.menu.on("save_as", lambda: self.save(True))
        self.menu.on("exit", self.editor.close_editor)

        self.menu.on("email", lambda: self.editor.load_snippet("email"))

        self.menu.on("enable_autosave", lambda: self.editor.start_autosave(15))
        self.menu.on("disable_autosave", self.editor.stop_autosave)

    def context_menu(self, e):
        self.click_menu.post(e.x_root, e.y_root)
