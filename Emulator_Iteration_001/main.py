from tkinter import*
import login_screen

#MainWindow Class
class MainWIndow(Tk):

    #Default initiaiser
    def __init__(self,master=None):
        Tk.__init__(self,master)
        self.geometry('1280x720')
        # self.geometry('1920x1080')
        self.config(bg="#000000")
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
        self.topLevelFrame= Frame(self,bg="white")
        
        #Info Frame
        self.infoFrame=Frame(self,bg="white")      

        #Child Frames of the Info Frame
        self.train_no=Frame(self.infoFrame,bg="#000000") 
        self.frame_title=Frame(self.infoFrame,bg="#00A2FF") 
        self.date_text=Frame(self.infoFrame,bg="#000000") 
        self.time_text=Frame(self.infoFrame,bg="#000000") 

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
        
        self.update()

    #Placing the widgets onto the main frame using the grid() method             
    def placeWidgets(self):
        #Top Level Frame
        self.topLevelFrame.grid(sticky=self.stickyValue,row=2,column=0,columnspan=11,padx=5,pady=5,rowspan=11)

        #info Frame
        self.infoFrame.grid(sticky=self.stickyValue, row=0,rowspan=1,column=0,columnspan=11,padx=5,pady=5)   
        
        #Buttons
        self.rowconfigure(1,minsize=self.winfo_height()/12)
        for (button,buttonIndex) in self.buttonArray.items():
            button.grid(sticky=self.stickyValue,row=1,column=buttonIndex-1,padx=5)      

        #Update geometry and configure the widgets
        self.update()
        self.configureWidgets()    

    #Configure widgets with essential attributes like commands, etc.
    def configureWidgets(self):
        
        #Info frame
        self.infoFrame.config(height=self.button01.winfo_height()/1.5, width=self.winfo_width()-10)

        self.update()

        #Top Level frame
        self.topLevelFrame.config(height=self.winfo_height() - self.button01.winfo_height() - self.infoFrame.winfo_height() - 20)

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
            frames.config(height=self.topLevelFrame.winfo_height()-6,width=self.topLevelFrame.winfo_width()-6)
        
        self.train_no.config(height=(self.infoFrame.winfo_height()-6),width=self.infoFrame.winfo_width()-6)   

        #Updating and testing
        self.update()        

    #An extra init function to declutter the default init. Makes the code more modular
    def initialiseWidgets(self):
        print("Initialising.....")

        self.train_no.grid(sticky=self.stickyValue, padx=3,pady=3)
    
    #Views one of the frames and makes all other frames invisible
    def viewFrame(self,frameIndex):
        for (frame,counter) in self.frameArray.items():
            if counter==frameIndex:
                frame.grid(sticky=self.stickyValue,padx=3,pady=3)
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

app=MainWIndow()
app.mainloop()
        
