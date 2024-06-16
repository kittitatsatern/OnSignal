import time
from SimpleSignal import Signal

class Door:
    def __init__(self) -> None:
        self.closing = Signal()
        self.closed = Signal()  

    def close_door(self):
        self.closing.fire()
        time.sleep(3)
        self.closed.fire()

def on_door_closing():
    print("Closing")

def on_door_closed():
    print("Closed")

new_door = Door()

new_door.closing.connect(on_door_closing)
new_door.closed.connect(on_door_closed)

new_door.close_door()