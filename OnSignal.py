class Signal:
    def __init__(self):
        self.callback = None

    def connect(self, callback):
        if not self.callback:
            self.callback = callback

    def disconnect(self):
        if self.callback:
            self.callback = None

    def fire(self, *args, **kwargs):
        if self.callback:
            self.callback(*args, **kwargs)

    def once(self, *args, **kwargs):
        if self.callback:
            self.fire(*args, **kwargs)
            self.disconnect()