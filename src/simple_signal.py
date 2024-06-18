class Connection:
    def __init__(self, signal, callback) -> None:
        self.signal = signal
        self.connected = True
        self.callback = callback
        self.next = None

    def disconnect(self):
        self.connected = False
        if self.signal:
            if self.signal.head == self:
                self.signal.head = self.next
            else:
                prev = self.signal.head
                while prev and prev.next != self:
                    prev = prev.next
                if prev:
                    prev.next = self.next
            self.signal = None
            self.callback = None
            self.next = None

    def __str__(self):
        return "Connection"

class Signal:
    def __init__(self) -> None:
        self.head = None
    
    def connect(self, callback):
        connection = Connection(self, callback)
        if self.head is None:
            self.head = connection
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = connection
        return connection
    
    def wait(self, callback):
        def wait_callback(*args):
            callback(*args)
            wait_connection.disconnect()
        wait_connection = self.connect(wait_callback)
        return wait_connection
    
    def disconnect_all(self):
        self.head = None
    
    def fire(self, *args):
        connection = self.head
        while connection:
            next_connection = connection.next
            if connection.connected:
                connection.callback(*args)
            connection = next_connection

    def __str__(self):
        return "Signal"