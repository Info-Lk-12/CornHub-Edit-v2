import platform
import threading
from playsound import playsound


def play_a_sound(*sound):
    def play():
        for s in sound:
            playsound(s)

    threading.Thread(target=play, daemon=False).start()
