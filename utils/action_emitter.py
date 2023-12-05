class Emitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)

    def _emit(self, event, *args):
        if event in self._listeners:
            for callback in self._listeners[event]:
                callback(*args)
