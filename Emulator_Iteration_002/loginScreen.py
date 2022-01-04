from tkinter import *

class Login(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.gridConfigure(3,1,self)
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()
    
    def createWidgets(self):
        self.userFrame = Frame(self, bg="red")
        self.keypadFrame = Frame(self, bg="blue")
    
    def configureWidgets(self):
        pass

    def placeWidgets(self):
        self.userFrame.grid(columnspan=1,rowspan=1,sticky="news")
        self.keypadFrame.grid(columnspan=1,rowspan=2,sticky="news")
    
    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1)
        for x in range(columns):
            root.columnconfigure(x,weight=1)

