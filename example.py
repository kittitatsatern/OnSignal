from src.SimpleSignal import Signal

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