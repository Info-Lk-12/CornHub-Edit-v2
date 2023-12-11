import os
import threading

from playsound import playsound


def play_a_sound(*sound, wd="assets"):
    def play():
        for s in sound:
            playsound(os.path.join(wd, s))

    threading.Thread(target=play, daemon=False).start()
