from tkinter import *
from resources import *


class MainWindow:
    def __init__(self):
        self.root=Tk()
        self.root.geometry('1000x700')
        self.root.config(bg="#000000")
        utils.placeGridConfigure(self,1,1,0,self.root)
        self.createWidgets()
        self.placeWidgets()
        self.root.mainloop()

    def createWidgets(self):
       self.button07=child_frames.ButtonHolder(self.root)
     
    def placeWidgets(self):
        utils.placeInGrid(self,self.button07,0,0)
        self.button07.configureWidgets()
        self.button07.placeWidgets()
        
    numberOfRows=1
    numberOfColumns=1

app=MainWindow()
    

