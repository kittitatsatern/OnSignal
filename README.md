# **Simple Signal**
I made this cool signal system in Python. It's totally thread-safe and uses weak references to handle connections and callbacks really well. You can connect things, disconnect them, pause callbacks, and start them again whenever you want.

## **How to Use**
Getting Started
```python
from simple_signal import Signal

# Create an instance of Signal
signal_instance = Signal()
```

Connecting a Callback
```python
def callback_function():
    print("Hello World.")

# Connect the callback function to the signal
signal_instance.connect(callback_function)
```

Firing the Signal
```python
# Fire the signal, triggering the connected callback
signal_instance.fire()
```