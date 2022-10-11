from tkinter import *

class Window(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.label = Label(text="Hello world!")
        self.label.pack(padx=10, pady=10)