from SimpleSignal import Signal

# Define a callback function
def callback(message):
    print(f"message: {message}")

# Create an instance of Signal
signal = Signal()

# Connect the callback function
signal.connect(callback)

# Fire the signal
signal.fire("Hello World.")

# Disconnect the callback
signal.disconnect()

# Trying to fire again won't do anything
signal.fire("This won't be received.")