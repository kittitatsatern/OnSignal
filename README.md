# **Simple Signal**
I made this cool signal system in Python. It's totally thread-safe and uses weak references to handle connections and callbacks really well. You can connect things, disconnect them, pause callbacks, and start them again whenever you want.

## **How to Use**
Example
```python
class Button:
    def __init__(self):
        self.clicked = Signal()

    def click(self):
        self.clicked.fire()

class Label:
    def __init__(self):
        self.text = ""

    def update_text(self, new_text):
        self.text = new_text
        print(f"Label updated to: {self.text}")

# Create a button and a label
button = Button()
label = Label()

# Connect the button click signal to the label update method
button.clicked.connect(lambda: label.update_text("Button clicked!"))

# Simulate a button click
button.click()
```