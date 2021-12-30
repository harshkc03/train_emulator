from tkinter import*

#MainWindow Class
class MainWIndow(Tk):

    #Default initiaiser
    def __init__(self,master=None):
        Tk.__init__(self,master)
        self.geometry('1200x675')
        self.config(bg="#000000")
        self.rowconfigure(1,minsize=60)
        self.createWidgets()
        self.placeWidgets()
        self.initialiseWidgets()    
    
    #Creating the necessary widgets that will remain embedded in the main Window
    def createWidgets(self):
        #RadioButtons
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

        #Dictionary having the buttons as objects     
        self.buttonArray={self.button01:1,
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
                                                            

        #Top level Frame
        self.topLevelFrame= Frame(bg="white")
        
        #Info Frame
        self.infoFrame=Frame(self,bg="#000000")       

        #Individual frames
        self.frame01=Frame(self.topLevelFrame,bg="#000000")
        self.frame02=Frame(self.topLevelFrame,bg="#000000")
        self.frame03=Frame(self.topLevelFrame,bg="#000000")
        self.frame04=Frame(self.topLevelFrame,bg="#000000")
        self.frame05=Frame(self.topLevelFrame,bg="#000000")
        self.frame06=Frame(self.topLevelFrame,bg="#000000")
        self.frame07=Frame(self.topLevelFrame,bg="#000000")
        self.frame08=Frame(self.topLevelFrame,bg="#000000")
        self.frame09=Frame(self.topLevelFrame,bg="#000000")
        self.frame10=Frame(self.topLevelFrame,bg="#000000")
        self.frame11=Frame(self.topLevelFrame,bg="#000000")

        #Dictionary having the frames as its objects
        self.frameArray={self.frame01:1,
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

    #Placing the widgets onto the main frame using the grid() method             
    def placeWidgets(self):
        #Top Level Frame
        self.topLevelFrame.grid(sticky=self.stickyValue,row=2,column=0,columnspan=11,padx=5,pady=5,rowspan=11)

        #info Frame
        self.infoFrame.grid(row=0,rowspan=1,column=0,columnspan=11)
        
        #Buttons
        for (button,buttonIndex) in self.buttonArray.items():
            button.grid(sticky=self.stickyValue,row=1,column=buttonIndex-1,padx=5)      

        #Update geometry and configure the widgets
        self.update()
        self.configureWidgets()    

    #Configure widgets with essential attributes like commands, etc.
    def configureWidgets(self):
        #Top Level frame
        self.topLevelFrame.config(height=self.button01.winfo_height()*9)        
        
        #Info frame
        self.infoFrame.config(width=self.winfo_width(),height=self.button01.winfo_height())

        #Buttons
        for (button,buttonValue) in self.buttonArray.items():
            button.config(variable=self.mainRadioButtonVariable,
                          value=buttonValue,indicatoron=0,
                          text="Text Button "+str(buttonValue),
                          bg="white",relief='flat')

        self.button01.config(command=self.button01Func)
        self.button02.config(command=self.button02Func)
        self.button03.config(command=self.button03Func)
        self.button04.config(command=self.button04Func)
        self.button05.config(command=self.button05Func)
        self.button06.config(command=self.button06Func)
        self.button07.config(command=self.button07Func)
        self.button08.config(command=self.button08Func)
        self.button09.config(command=self.button09Func)
        self.button10.config(command=self.button10Func)
        self.button11.config(command=self.button11Func)       

        self.update()

        #Child Frames
        for (frames) in self.frameArray:
            frames.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())        

        #Updating and testing
        self.update()        
        self.testWidgetGeometry()

    #An extra init function to declutter the default init. Makes the code more modular
    def initialiseWidgets(self):
        print("Initialising.....")
    
    #Views one of the frames and makes all other frames invisible
    def viewFrame(self,frameIndex):
        for (frame,counter) in self.frameArray.items():
            if counter==frameIndex:
                frame.grid(sticky=self.stickyValue,padx=2,pady=2)
            else:
                frame.grid_remove()                

    #Button Functions
    def button01Func(self):
        print("Button 1 is pressed")
        self.viewFrame(1)
                    
    def button02Func(self):
        print("Button 2 is pressed")
        self.viewFrame(2)        
        
    def button03Func(self):
        print("Button 3 is pressed")
        self.viewFrame(3)       

    def button04Func(self):
        print("Button 4 is pressed")
        self.viewFrame(4)

    def button05Func(self):
        print("Button 5 is pressed")
        self.viewFrame(5)

    def button06Func(self):
        print("Button 6 is pressed")
        self.viewFrame(6)
        
    def button07Func(self):
        print("Button 7 is pressed")
        self.viewFrame(7)

    def button08Func(self):
        print("Button 8 is pressed")
        self.viewFrame(8)

    def button09Func(self):
        print("Button 9 is pressed")
        self.viewFrame(9)    

    def button10Func(self):
        print("Button 10 is pressed")
        self.viewFrame(10)
        
    def button11Func(self):
        print("Button 11 is pressed")
        self.viewFrame(11)
   
    #Variables
    mainRadioButtonVariable=1
    stickyValue="news"
    topLevelFrameHeight=900
    

app=MainWIndow()
app.mainloop()
        
