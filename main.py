from editor import Editor
from window import CornHubEditWindow


def main():
    editor = Editor()
    app = CornHubEditWindow(editor)
    # code here

    app.mainloop()


if __name__ == "__main__":
    main()
