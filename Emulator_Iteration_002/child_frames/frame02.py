import imp
from tkinter import*

class Frame02(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,bg="pink")
        print("child frame has been created")
