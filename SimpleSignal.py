class Signal:
    def __init__(self):
        self.callback = None

    # connect a callback function to the signal.
    def connect(self, callback):
        self.callback = callback

    # wait for a single fire event and then disconnect the callback.
    def wait(self, callback):
        self.connect(callback)
        self.waiting = True
            
    # disconnect currently connected callback.
    def disconnect(self):
        self.callback = None
        if self.waiting:
            self.waiting = None

    # trigger the connected callback function.
    def fire(self, *args, **kwargs):
         if self.callback:
            self.callback(*args, **kwargs)
            if self.waiting:
                self.disconnect()

    # fire the signal once and then disconnect the callback.
    def once(self, *args, **kwargs):
        self.fire(*args, **kwargs)
        self.disconnect()
    
    def __str__(self):
        return "Signal"