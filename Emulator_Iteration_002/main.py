from tkinter import *

class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("1200x625")
        self.config(bg="#000000")
        self.gridConfigure(self.numberOfRows,self.numberOfColumns,self)
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()

    def createWidgets(self):
        #Info frame
        self.infoFrame=Frame(self,bg="white")

        #Info Frame Children
        self.trainNoFrame=Frame(self.infoFrame,bg="#000000")
        self.titleFrame=Frame(self.infoFrame,bg="#000000")
        self.dateFrame=Frame(self.infoFrame,bg="#000000")
        self.timeFrame=Frame(self.infoFrame,bg="#000000")

        #Buttons
        self.button01=Radiobutton(self)
        self.button02=Radiobutton(self)
        self.button03=Radiobutton(self)
        self.button04=Radiobutton(self)
        self.button05=Radiobutton(self)
        self.button06=Radiobutton(self)
        self.button07=Radiobutton(self)
        self.button08=Radiobutton(self)
        self.button09=Radiobutton(self)
        self.button10=Radiobutton(self)
        self.button11=Radiobutton(self)

        #Parent frame for all sub frames
        self.topLevelFrame=Frame(self,bg="white")

        #Dictionary containing buttons and an index
        self.buttonDict={self.button01:1,
                         self.button02:2,
                         self.button03:3,
                         self.button04:4,
                         self.button05:5,
                         self.button06:6,
                         self.button07:7,
                         self.button08:8,
                         self.button09:9,
                         self.button10:10,
                         self.button11:11}

    def configureWidgets(self):
        self.gridConfigure(1,self.numberOfColumns,self.infoFrame)

        for button,index in self.buttonDict.items():
            button.config(text="Button "+str(index),value=index,indicatoron=0,variable=self.mainRadioButtonVar,relief='flat',bg="#FFFFFF")
                
        self.gridConfigure(self.numberOfRows-2,self.numberOfColumns,self.topLevelFrame)
        
    def placeWidgets(self):
        #infoFrame
        self.infoFrame.grid(row=0,column=0,columnspan=self.numberOfColumns,padx=2,sticky="news",pady=2)

        #info Frame Children
        self.trainNoFrame.grid(row=0,column=0,columnspan=2,padx=2,pady=2,sticky="news")
        self.titleFrame.grid(row=0,column=2,columnspan=5,padx=2,pady=2,sticky="news")
        self.dateFrame.grid(row=0,column=7,columnspan=2,padx=2,pady=2,sticky="news")
        self.timeFrame.grid(row=0,column=9,columnspan=2,padx=2,pady=2,sticky="news")

        #Buttons
        for button,index in self.buttonDict.items():
            button.grid(row=1,column=index-1,sticky="news",padx=2)

        #TopLevelFrame
        self.topLevelFrame.grid(row=2,rowspan=self.numberOfRows-2,column=0,columnspan=self.numberOfColumns,sticky="news",padx=2,pady=2)

    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1)
        for x in range(columns):
            root.columnconfigure(x,weight=1)
    
    #Variables
    numberOfRows=12
    numberOfColumns=11
    mainRadioButtonVar=1


app=MainWindow()
app.mainloop()