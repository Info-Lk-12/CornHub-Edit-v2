import platform
import threading

if platform.system() == "Windows":
    from winsound import PlaySound, SND_FILENAME


def play_a_sound(*sound):
    def play_win():
        for s in sound:
            PlaySound(s, SND_FILENAME)

    if platform.system() == "Windows":
        threading.Thread(target=play_win, daemon=False).start()
