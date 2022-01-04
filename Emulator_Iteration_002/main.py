from tkinter import *
import datetime
import loginScreen

class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry("1200x625")
        self.config(bg="#000000")
        self.gridConfigure(self.numberOfRows,self.numberOfColumns,self)
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()
        self.after(0, self.update_clock)

    def createWidgets(self):
        #Info frame
        self.infoFrame=Frame(self,bg="white")

        #Info Frame Children
        self.trainNoFrame=Frame(self.infoFrame,bg="#000000")
        self.titleFrame=Frame(self.infoFrame,bg="#000000")
        self.dateFrame=Frame(self.infoFrame,bg="#000000")
        self.timeFrame=Frame(self.infoFrame,bg="#000000")

        #Info Frame Labels
        self.trainNoLabel=Label(self.trainNoFrame,text="Train No. 14569",bg="#000000",fg="#FFFFFF")
        self.titleLabel=Label(self.titleFrame,text="Title",bg="#000000",fg="#FFFFFF")
        self.dateLabel=Label(self.dateFrame,text=str(datetime.datetime.today().strftime('%d/%m/%Y')),bg="#000000",fg="#FFFFFF")
        self.timeLabel=Label(self.timeFrame,text=str(datetime.datetime.now().strftime("%H:%M:%S")),bg="#000000",fg="#FFFFFF")

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

        #Sub Frames
        self.frame01=loginScreen.Login(master=self.topLevelFrame)
        self.frame02=Frame(master=self.topLevelFrame)
        self.frame03=Frame(master=self.topLevelFrame)
        self.frame04=Frame(master=self.topLevelFrame)
        self.frame05=Frame(master=self.topLevelFrame)
        self.frame06=Frame(master=self.topLevelFrame)
        self.frame07=Frame(master=self.topLevelFrame)
        self.frame08=Frame(master=self.topLevelFrame)
        self.frame09=Frame(master=self.topLevelFrame)
        self.frame10=Frame(master=self.topLevelFrame)
        self.frame11=Frame(master=self.topLevelFrame)

        
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

        #Dictionary containing frames and an index
        self.frameDict={self.frame01:1,
                        self.frame02:2,
                        self.frame03:3,
                        self.frame04:4,
                        self.frame05:5,
                        self.frame06:6,
                        self.frame07:7,
                        self.frame08:8,
                        self.frame09:9,
                        self.frame10:10,
                        self.frame11:11,}

    def configureWidgets(self):
        #info Frame grid configuration
        self.gridConfigure(1,self.numberOfColumns,self.infoFrame)

        #info Frame Children grid configuration
        self.gridConfigure(1,1,self.trainNoFrame)
        self.gridConfigure(1,1,self.titleFrame)
        self.gridConfigure(1,1,self.dateFrame)
        self.gridConfigure(1,1,self.timeFrame)

        #configuring buttons
        for button,index in self.buttonDict.items():
            button.config(text="Button "+str(index),value=index,indicatoron=0,
                          variable=self.mainRadioButtonVar,relief='flat',
                          bg="#FFFFFF",offrelief='flat',command=lambda temp=index: self.displayFrame(temp))

        #configuring topLevelFrame grid       
        self.gridConfigure(self.numberOfRows-2,self.numberOfColumns,self.topLevelFrame)

        #configuring sub frames of topLevelFrame
        for frame in self.frameDict:
            frame.config(bg="#000000")
            self.gridConfigure(self.numberOfRows-2,self.numberOfColumns,frame)
        
    def placeWidgets(self):
        #infoFrame
        self.infoFrame.grid(row=0,column=0,columnspan=self.numberOfColumns,sticky="news",pady=2)

        #info Frame Children
        self.trainNoFrame.grid(row=0,column=0,columnspan=2,padx=2,pady=2,sticky="news")
        self.titleFrame.grid(row=0,column=2,columnspan=5,padx=2,pady=2,sticky="news")
        self.dateFrame.grid(row=0,column=7,columnspan=2,padx=2,pady=2,sticky="news")
        self.timeFrame.grid(row=0,column=9,columnspan=2,padx=2,pady=2,sticky="news")

        #info Frame Labels
        self.trainNoLabel.grid(sticky="news")
        self.titleLabel.grid(sticky="news")
        self.dateLabel.grid(sticky="news")
        self.timeLabel.grid(sticky="news")

        #Buttons
        for button,index in self.buttonDict.items():
            button.grid(row=1,column=index-1,sticky="news",padx=2)

        #TopLevelFrame
        master=self.topLevelFrame.grid(row=2,rowspan=self.numberOfRows-2,
                                       column=0,columnspan=self.numberOfColumns,
                                       sticky="news",pady=2)

    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1)
        for x in range(columns):
            root.columnconfigure(x,weight=1)
    
    def displayFrame(self,frameIndex):
        for frame,index in self.frameDict.items():
            if index==frameIndex:
                frame.grid(rowspan=self.numberOfRows-2,columnspan=self.numberOfColumns,padx=2,pady=2,sticky="news",row=0)
            else:
                frame.grid_remove()

    def update_clock(self):
        self.timeLabel.config(text=str(datetime.datetime.now().strftime("%H:%M:%S")))
        self.after(1000, self.update_clock)

    #Variables
    numberOfRows=12
    numberOfColumns=11
    mainRadioButtonVar=1


app=MainWindow()
app.mainloop()