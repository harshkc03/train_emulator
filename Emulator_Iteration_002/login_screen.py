from tkinter import*

class Login(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,bg="blue")
        self.gridConfigure(3,1,self)
        self.createWidgets()
        # self.configureWidgets()
        self.placeWidgets()

    def createWidgets(self):
        self.entryFrame=Frame(self,bg="pink")
        self.keyPadFrame=Frame(self,bg="red")

    # def configureWidgets(self):
    #     self.gridConfigure(2,5,self.entryFrame)
    #     self.gridConfigure(4,3,self.keyPadFrame)

    def placeWidgets(self):
        self.entryFrame.grid(row=0,sticky="news")
        self.keyPadFrame.grid(row=1,rowspan=2,sticky="news")

    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1)
        for x in range(columns):
            root.columnconfigure(x,weight=1)
    