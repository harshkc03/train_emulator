from tkinter import *

class ModeSelect(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.gridConfigure(3,3,self)
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()
    
    def createWidgets(self):
        self.manualFrame=Frame(self,bg="#000000")
        self.recreateFrame=Frame(self,bg="#000000")
        self.autoFrame=Frame(self,bg="#000000")
        self.currentFrame=Frame(self,bg="#000000")

        self.manualButton=Radiobutton(self.manualFrame)
        self.recreateButton=Radiobutton(self.recreateFrame)
        self.autoButton=Radiobutton(self.autoFrame)

        self.buttonDict={self.manualButton:1,
                         self.recreateButton:2,
                         self.autoButton:3}
        
        self.buttonNames={1:"Manual",
                          2:"Recreate",
                          3:"Auto"}
        
        self.currentLabel=Label(self.currentFrame)
    
    def configureWidgets(self):
        for button,index in self.buttonDict.items():
            button.config(text=self.buttonNames[index],value=index,indicatoron=0,
                          variable=self.mainRadioButtonVar,relief='flat',
                          bg="#FFFFFF",offrelief='flat',command=lambda temp=index: self.buttonFunc(temp))
        
        self.currentLabel.config(text="Current Mode: \t",fg="#000000",bg="#FFFFFF",borderwidth=4,relief="solid",highlightbackground="red")

    def placeWidgets(self):
        self.manualFrame.grid(rowspan=2, column=0,sticky="nsew",row=0)
        self.recreateFrame.grid(rowspan=2,column=1,sticky="nsew",row=0)
        self.autoFrame.grid(rowspan=2,column=2,sticky="nsew",row=0)
        self.currentFrame.grid(row=2,columnspan=3,sticky="news")

        for button,index in self.buttonDict.items():
            button.place(relx=0.5,rely=0.7,anchor="center",relheight=0.3,relwidth=0.5)
        
        self.currentLabel.place(relx=0.5,rely=0.5,anchor="center",relheight=0.3,relwidth=0.2)
    
    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1)
        for x in range(columns):
            root.columnconfigure(x,weight=1)
    
    def buttonFunc(self, mode):
        self.currentLabel.config(text="Current Mode: "+self.buttonNames[mode])

    mainRadioButtonVar=2

