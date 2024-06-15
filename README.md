# **OnSignal**
A simple way to handle callbacks in Python, allow you to connect function (callback) and trigger them with when necessary.

## **Example**
Example
```python
from OnSignal import Signal

signal = Signal()

signal.connect(lambda : print("Hi"))

signal.fire()
```

## **How to Use**
Getting Started
```python
from OnSignal import Signal

# Create an instance of Signal
signal_instance = Signal()
```

Connecting a Callback
```python
def callback_function(arg1, arg2):
    print("Called!")

# Connect the callback function to the signal
signal_instance.connect(callback_function)
```

Firing the Signal
```python
# Fire the signal, triggering the connected callback
signal_instance.fire()
```
