from tkinter import *
from tkinter import ttk
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
    #    self.bar=child_frames.Indicator(self.root,self.root,"Current","Red","22","A")
        self.bar=Canvas()
     
    def placeWidgets(self):
        utils.placeInGrid(self,self.bar,0,0)
        
        
    numberOfRows=1
    numberOfColumns=1

app=MainWindow()
    

