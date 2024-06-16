# **Simple Signal**
A simple way to handle callback in Python, allow you to connect function (callback) and trigger them with when necessary.

## **How to Use**
Getting Started
```python
from SimpleSignal import Signal

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
