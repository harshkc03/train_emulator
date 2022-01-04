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

        self.userIDLabel = Label(self.userFrame, text="User ID:", bg="#000000", fg="#FFFFFF")
        self.entryLabel = Label(self.userFrame, text="Entry", bg="#000000", fg="#FFFFFF")
    
    def configureWidgets(self):
        self.gridConfigure(2,3,self.userFrame)
        self.gridConfigure(4,3,self.keypadFrame)

    def placeWidgets(self):
        # self.userFrame.grid(sticky="news",row=1,column=4,rowspan=2,columnspan=8)
        # self.keypadFrame.grid(sticky="news",row=4,column=6,rowspan=4,columnspan=4)

        self.userFrame.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.25, anchor=CENTER)
        self.keypadFrame.place(relx=0.5, rely=0.7, relwidth=0.25, relheight=0.45, anchor=CENTER)

        self.userIDLabel.grid(sticky="news",row=0,column=0,rowspan=2,columnspan=1,padx=2,pady=2)
        self.entryLabel.grid(sticky="news",row=0,column=1,rowspan=1,columnspan=1,padx=2,pady=2)
    
    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x)
            root.grid_rowconfigure(x, weight=1, uniform="fred")
        for x in range(columns):
            root.columnconfigure(x)
            root.grid_columnconfigure(x, weight=1, uniform="fred")

