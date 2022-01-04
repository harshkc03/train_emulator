from tkinter import *

class Login(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.gridConfigure(9,16,self)
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()
    
    def createWidgets(self):
        self.userFrame = Frame(self, bg="red")
        self.keypadFrame = Frame(self, bg="blue")
    
    def configureWidgets(self):
        pass

    def placeWidgets(self):
        self.userFrame.grid(sticky="news",row=1,column=4,rowspan=2,columnspan=8)
        self.keypadFrame.grid(sticky="news",row=4,column=6,rowspan=4,columnspan=4)
    
    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1)
        for x in range(columns):
            root.columnconfigure(x,weight=1)

