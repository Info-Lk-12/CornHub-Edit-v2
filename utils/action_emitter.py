class Emitter:
    def __init__(self):
        self.listeners = {}

    def on(self, event, callback):
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(callback)

    def _emit(self, event, *args):
        if event in self.listeners:
            for callback in self.listeners[event]:
                callback(*args)
