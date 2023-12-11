import os

from editor import Editor
from window import CornHubEditWindow
from utils.sound_mgr import play_a_sound

working_dir = os.path.dirname(os.path.realpath(__file__))
asset_path = os.path.join(working_dir, "assets")


def main():
    # play_a_sound("phintro.wav", wd=asset_path)

    editor = Editor()
    app = CornHubEditWindow(editor)
    app.mainloop()

    # play_a_sound("phoutro.wav", wd=asset_path)


if __name__ == "__main__":
    main()
