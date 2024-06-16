class Connection:
    def __init__(self, signal, callback) -> None:
        self.signal = signal
        self.connected = True
        self.callback = callback
        self.prev = None
        self.next = None

    def disconnect(self):
        self.connected = False
        if self.signal:
            if self.signal.head == self:
                self.signal.head = self.next
            if self.signal.tail == self:
                self.signal.tail = self.prev
            if self.prev:
                self.prev.next = self.next
            if self.next:
                self.next.prev = self.prev
            self.prev = None
            self.next = None

    def __str__(self):
        return "Connection"

class Signal:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def connect(self, callback):
        connection = Connection(self, callback)
        if self.tail:
            self.tail.next = connection
            connection.prev = self.tail
        else:
            self.head = connection
        self.tail = connection
        return connection

    def wait(self, callback):
        def wait_callback(*args):
            callback(*args)
            wait_connection.disconnect()
        wait_connection = self.connect(wait_callback)
        return wait_connection

    def disconnect_all(self):
        self.head = None
        self.tail = None

    def fire(self, *args):
        connection = self.head
        while connection:
            next_connection = connection.next
            if connection.connected:
                connection.callback(*args)
            connection = next_connection

    def __str__(self):
        return "Signal"