from SimpleSignal import Signal

# Define a callback function
def callback(message):
    print(f"message: {message}")

def callback2(message):
    print(f"message2: {message}")

# Create an instance of Signal
signal = Signal()

# Connect the callback function
connection = signal.connect(callback)
signal.connect(callback2)

connection.disconnect()

# Fire the signal
signal.fire("Hello World.")

# Disconnect the callback
signal.disconnect_all()

# Trying to fire again won't do anything
signal.fire("This won't be received.")