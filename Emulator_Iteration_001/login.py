from tkinter import *

class loginFrame(Frame):

    nrows = 8
    ncols = 10

    def __init__(self,window):
        Frame.__init__(self,window)

        self.config(bg="red")
