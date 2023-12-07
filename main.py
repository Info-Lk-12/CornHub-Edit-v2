from editor import Editor
from window import CornHubEditWindow
from utils.sound_mgr import play_a_sound

def main():
    play_a_sound("assets/phintro.wav")
    editor = Editor()
    app = CornHubEditWindow(editor)
    # code here

    app.mainloop()


if __name__ == "__main__":
    main()
