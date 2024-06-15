class Signal:
    def __init__(self):
        self.callback = None

    # connect a callback function to the signal
    def connect(self, callback):
        if not self.callback:
            self.callback = callback
            
    # disconnects currently connected callback
    def disconnect(self):
        if self.callback:
            self.callback = None

    # trigger the connected callback function.
    def fire(self, *args, **kwargs):
        if self.callback:
            self.callback(*args, **kwargs)

    # fire the signal once and then disconnect the callback
    def once(self, *args, **kwargs):
        if self.callback:
            self.fire(*args, **kwargs)
            self.disconnect()