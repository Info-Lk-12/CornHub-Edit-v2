import threading
from time import sleep

from utils.action_emitter import Emitter


class Editor(Emitter):
    def __init__(self):
        super().__init__()
        self._text = ""
        self.path = None
        self.autosave_on = False

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self._emit("change")

    def new_file(self):
        self.text = ""

    def open_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.text = file.read()
                self.path = file_path
        except FileNotFoundError:
            print(f"File not found: {file_path}")

    def save_as_file(self, file_path):
        try:
            with open(file_path, 'w') as file:
                file.write(self.text)
                self.path = file_path
        except Exception as e:
            print(f"Error saving file: {e}")

    def save_file(self):
        if self.path is None or self.path == "":
            raise Exception('Document not found')
        else:
            try:
                with open(self.path, 'w') as file:
                    file.write(self.text)
            except Exception as e:
                print(f"Error saving file: {e}")

    def cut_text(self, start, end):
        selected_text = self.text[start:end]
        self.clipboard = selected_text
        self.text = self.text[:start] + self.text[end:]

    def copy_text(self, start, end):
        selected_text = self.text[start:end]
        self.clipboard = selected_text

    def paste_text(self, start):
        self.text = self.text[:start] + self.clipboard + self.text[start:]

    def close_editor(self):
        exit()

    def autosave(self, interval):
        self.autosave_on = True
        while self.autosave_on:
            if self.path is not None and self.path != "":
                self.save_file()
            sleep(interval)

    def start_autosave(self, interval):
        threading.Thread(target=self.autosave, args=(interval,), daemon=True).start()

    def stop_autosave(self):
        self.autosave_on = False

    def email_snippet(self):
        self.text = "Sehr geehrter Herr/Frau," \
                    "\n\n" \
                    "[Text hier einfügen]" \
                    "\n\n" \
                    "Mit freundlichen Grüßen"
