from tkinter import*
import datetime
import login_screen

import test_gui

import login.gui

#MainWindow Class
class MainWIndow(Tk):

    #Default initiaiser
    def __init__(self,master=None):
        Tk.__init__(self,master)
        self.geometry('1280x720')
        self.attributes("-fullscreen",True)
        self.config(bg="#000000")
        self.createWidgets()
        self.placeWidgets()
        self.initialiseWidgets()    
        #self.loginInit()
    
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
        self.frame_title=Frame(self.infoFrame,bg="#000000") 
        self.date_text=Frame(self.infoFrame,bg="#000000") 
        self.time_text=Frame(self.infoFrame,bg="#000000") 

        #Labels
        self.train_label=Label(self.train_no,text="Train: 69145",bg="#000000",fg="white")
        self.frame_label=Label(self.frame_title,text="",bg="#000000",fg="white")
        self.date_label=Label(self.date_text,text=str(datetime.datetime.today().strftime('%d/%m/%Y')),bg="#000000",fg="white")
        self.time_label=Label(self.time_text,text=str(datetime.datetime.now().strftime("%H:%M:%S")),bg="#000000",fg="white")

        #Info frame child dictionary
        self.infoFrameChild={self.train_no:1,
                        self.frame_title:2,
                        self.date_text:3,
                        self.time_text:4}

        #Individual frames
        self.frame01=Frame(self.topLevelFrame,bg="#000000")
        self.frame02=test_gui.test_frame(self.topLevelFrame)
        self.frame03=login.gui.login_frame(self.topLevelFrame)
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
             
        #info Frame
        self.infoFrame.grid(sticky=self.stickyValue, row=0,rowspan=1,column=0,columnspan=11,padx=5,pady=5) 
        self.train_no.grid(row=0,column=0,columnspan=2,sticky=self.stickyValue,padx=2,pady=2)
        self.frame_title.grid(row=0,column=2,columnspan=5,sticky=self.stickyValue,padx=2,pady=2)
        self.date_text.grid(row=0,column=7,columnspan=2,sticky=self.stickyValue,padx=2,pady=2)
        self.time_text.grid(row=0,column=9,columnspan=2,sticky=self.stickyValue,padx=2,pady=2)

        self.train_label.place(anchor=CENTER,relx=0.5,rely=0.5)
        self.frame_label.place(anchor=CENTER,relx=0.5,rely=0.5)
        self.date_label.place(anchor=CENTER,relx=0.5,rely=0.5)
        self.time_label.place(anchor=CENTER,relx=0.5,rely=0.5)

        #Buttons
        self.rowconfigure(1,minsize=self.winfo_height()/12)
        for (button,buttonIndex) in self.buttonArray.items():
            button.grid(sticky=self.stickyValue,row=1,column=buttonIndex-1,padx=5) 

        #Top Level Frame
        self.topLevelFrame.grid(sticky=self.stickyValue,row=2,column=0,columnspan=11,padx=5,pady=5,rowspan=11)      
              
        #Update geometry and configure the widgets
        self.update()
        self.configureWidgets()    

    #Configure widgets with essential attributes like commands, etc.
    def configureWidgets(self):
        
        #Info frame
        self.infoFrame.config(height=self.button01.winfo_height()/1.5, width=self.winfo_width()-10)

        self.update()

        for frame in self.infoFrameChild:
            frame.config(height=self.button01.winfo_height()/1.5)

        self.train_no.config(width=(self.winfo_width()/11)*2-6)
        self.frame_title.config(width=(self.winfo_width()/11)*5-6)
        self.date_text.config(width=(self.winfo_width()/11)*2-6)
        self.time_text.config(width=(self.winfo_width()/11)*2-6)

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

        #Updating and testing
        self.update()        

    #An extra init function to declutter the default init. Makes the code more modular
    def initialiseWidgets(self):
        print("Initialising.....")

        self.after(0, self.update_clock)

    #Login implementation
    # def loginInit(self):
    #     for button in self.buttonArray:
    #         button.config(state='disabled')
    #     self.login=login_screen.Login(self.topLevelFrame)

        
    #Views one of the frames and makes all other frames invisible
    def viewFrame(self,frameIndex):

        for (frame,counter) in self.frameArray.items():
            if counter==frameIndex:
                frame.grid(sticky=self.stickyValue,padx=3,pady=3)
                self.frame_label.config(text="Frame "+str(frameIndex))
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

    def update_clock(self):
        self.time_label.config(text=str(datetime.datetime.now().strftime("%H:%M:%S")))
        self.after(1000, self.update_clock)
   
    #Variables
    mainRadioButtonVariable=1
    stickyValue="news"   

app=MainWIndow()
app.mainloop()
        
