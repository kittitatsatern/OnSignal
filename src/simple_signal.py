import weakref
import threading

class Connection:
    def __init__(self, signal, callback) -> None:
        self.signal = weakref.ref(signal)()
        self.connected = True
        self.callback = callback
        self.next = None
        self.lock = threading.RLock()

    """ Disconnects the callback from the signal """
    def disconnect(self) -> bool:
        with self.lock:
            self.connected = False
            signal = self.signal
            if signal:
                with signal.lock:
                    if signal.head == self:
                        signal.head = self.next
                    else:
                        prev = signal.head
                        while prev and prev.next != self:
                            prev = prev.next
                        if prev:
                            prev.next = self.next
            self.signal = None
            self.callback = None
            self.next = None
            return True

    """ Pauses the connection, preventing the callback from being called """
    def pause(self):
        with self.lock:
            self.connected = False

    """ Resumes the connection, allowing the callback to be called """
    def resume(self):
        with self.lock:
            self.connected = True

    def __str__(self):
        return "Connection"

class Signal:
    def __init__(self) -> None:
        self.head = None
        self.lock = threading.RLock()
    
    """ Connects a callback to the signal and returns a "Connection" object """
    def connect(self, callback):
        with self.lock:
            connection = Connection(self, callback)
            if not self.head:
                self.head = connection
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = connection
            return connection
    
    """ Connects a callback to the signal that will be disconnected after being called once """
    def wait(self, callback):
        def wrapper(*args):
            callback(*args)
            wrapper_connection.disconnect()
        wrapper_connection = self.connect(wrapper)
        return wrapper_connection
    
    """ Disconnects all callbacks from the signal """
    def disconnect_all(self) -> bool:
        with self.lock:
            self.head = None
            return True
    
    """ Fires the signal, calling all connected callbacks """
    def fire(self, *args):
        connection = self.head
        while connection:
            with connection.lock:
                if connection.connected:
                    connection.callback(*args)
            connection = connection.next
    
    """ Fires the signal once and then disconnects all callbacks """
    def once(self, *args):
        self.fire(*args)
        self.disconnect_all()

    """ Pauses all connections, preventing all callbacks from being called """
    def pause_all(self):
        with self.lock:
            current = self.head
            while current:
                if current.connected:
                    current.pause()
                current = current.next

    """ Resumes all connections, allowing all callbacks to be called """
    def resume_all(self):
        with self.lock:
            current = self.head
            while current:
                if not current.connected:
                    current.resume()
                current = current.next

    def __str__(self):
        return "Signal"