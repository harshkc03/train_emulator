import login_screen
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
        self.initWidgets()
        self.launchLogin()

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

        #Sub Frames
        self.frame01=Frame(master=self.topLevelFrame)
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

        #Login
        self.loginFrame=login_screen.Login(self.frame01,self)

        
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
                        self.frame11:11}

    def configureWidgets(self):
        #info Frame grid configuration
        self.gridConfigure(1,self.numberOfColumns,self.infoFrame)

        #configuring buttons
        for button,index in self.buttonDict.items():
            button.config(text="Button "+str(index),value=index,indicatoron=0,
                          variable=self.mainRadioButtonVar,relief='flat',
                          bg="#FFFFFF",offrelief='flat',command=lambda temp=index : self.displayFrame(temp))
        

        #configuring topLevelFrame grid       
        self.gridConfigure(self.numberOfRows-2,self.numberOfColumns,self.topLevelFrame)

        #Configuring frame 01 grid
        self.gridConfigure(self.numberOfRows-2,self.numberOfColumns,self.frame01)

        #configuring sub frames of topLevelFrame
        for frame in self.frameDict:
            frame.config(bg="#000000")
                    
    def placeWidgets(self):
        #infoFrame
        self.infoFrame.grid(row=0,column=0,columnspan=self.numberOfColumns,sticky="news",pady=2)

        #info Frame Children
        self.trainNoFrame.grid(row=0,column=0,columnspan=2,padx=2,pady=2,sticky="news")
        self.titleFrame.grid(row=0,column=2,columnspan=5,padx=2,pady=2,sticky="news")
        self.dateFrame.grid(row=0,column=7,columnspan=2,padx=2,pady=2,sticky="news")
        self.timeFrame.grid(row=0,column=9,columnspan=2,padx=2,pady=2,sticky="news")

        #Buttons
        for button,index in self.buttonDict.items():
            button.grid(row=1,column=index-1,sticky="news",padx=2)

        #TopLevelFrame
        self.topLevelFrame.grid(row=2,rowspan=self.numberOfRows-2,
                                       column=0,columnspan=self.numberOfColumns,
                                       sticky="news",pady=2)

        self.loginFrame.grid(row=0,rowspan=(self.numberOfRows-2),column=3,columnspan=5,sticky="news")

    def initWidgets(self):
        print("Initializing......")
       
    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1,minsize=(root.winfo_height()/rows))
        for x in range(columns):
            root.columnconfigure(x,weight=1,minsize=(root.winfo_width()/columns))
    
    def displayFrame(self,frameIndex):
        for (frame,index) in self.frameDict.items():
            if index==frameIndex:
                frame.grid(row=0,column=0,rowspan=self.numberOfRows-2,columnspan=self.numberOfColumns,
               padx=2,pady=2,sticky="news")
            else:
                frame.grid_remove()

    def launchLogin(self):
        print("launching login")  

        self.button01.invoke()
        self.disableButtonsExcept([1])

        self.startTasks()
    
    def disableButtonsExcept(self,buttonsToBeLeft):      

        for button in self.buttonDict:
            if self.buttonDict[button] not in buttonsToBeLeft:
                button.config(state="disabled")
            else:
                button.config(state="normal")

    def setState(self,state):
        if state == "Driver":
            self.disableButtonsExcept([1,3,5,7,9,11])
        elif state == "Maintenance":
            self.enableAll()
        elif state=="Exit":
            quit()

    def enableAll(self):
        for button in self.buttonDict:
            button.config(state="normal")
                    
    def startTasks(self):
        print("Starting all tasks..")
     

    #Variables
    numberOfRows=12
    numberOfColumns=11
    mainRadioButtonVar=1


app=MainWindow()
app.mainloop()