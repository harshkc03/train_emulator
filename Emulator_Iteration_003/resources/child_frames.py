from cgitb import text
from tkinter import *
import datetime
import sys
from resources import utils

class InfoFrame(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,bg="white")
        utils.gridConfigure(1,11,self)
        self.createWidgets()
        self.placeWidgets()
        self.initTime()

    def createWidgets(self):
        #Info Frame Children
        self.trainNoFrame=Frame(self,bg="#000000")
        self.train_label=Label(self.trainNoFrame,text="Train: 69145",bg="#000000",fg="white",font=self.defaultFont)

        self.titleFrame=Frame(self,bg="#000000")
        self.frame_label=Label(self.titleFrame,text="",bg="#000000",fg="white",font=self.defaultFont)

        self.modeFrame=Frame(self,bg="#000000")
        self.modeLabel=Label(self.modeFrame,text="Select mode!",bg="#000000",fg="white",font=self.defaultFont)

        self.dateFrame=Frame(self,bg="#000000")
        self.date_label=Label(self.dateFrame,text=str(datetime.datetime.today().strftime('%d/%m/%Y')),bg="#000000",fg="white",font=self.defaultFont)

        self.timeFrame=Frame(self,bg="#000000")      
        self.time_label=Label(self.timeFrame,text=str(datetime.datetime.now().strftime("%H:%M:%S")),bg="#000000",fg="white",font=self.defaultFont)
        
    def placeWidgets(self):
        
        #info Frame Children
        self.trainNoFrame.grid(row=0,column=0,columnspan=2,padx=2,pady=2,sticky="news")
        self.titleFrame.grid(row=0,column=2,columnspan=3,padx=2,pady=2,sticky="news")
        self.modeFrame.grid(row=0,column=5,columnspan=2,padx=2,pady=2,sticky="news")
        self.dateFrame.grid(row=0,column=7,columnspan=2,padx=2,pady=2,sticky="news")
        self.timeFrame.grid(row=0,column=9,columnspan=2,padx=2,pady=2,sticky="news")

        self.train_label.place(anchor='center',relx=0.5,rely=0.5)
        self.frame_label.place(anchor='center',relx=0.5,rely=0.5)
        self.date_label.place(anchor='center',relx=0.5,rely=0.5)
        self.time_label.place(anchor='center',relx=0.5,rely=0.5)
        self.modeLabel.place(anchor='center',relx=0.5,rely=0.5)

    def initTime(self):
        self.after(0, self.update_clock)

    def update_clock(self):
        self.time_label.config(text=str(datetime.datetime.now().strftime("%H:%M:%S")))
        self.after(1000, self.update_clock)

    defaultFont="Calibri 15"

class ButtonHolder(Frame):
    def __init__(self,master):
        self.master=master
        Frame.__init__(self,master,bg="black")
        self.createWidgets()

    def createWidgets(self):
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

        #Dictionary containing buttons and an index
        self.buttonDict={1:self.button01,
                         2:self.button02,
                         3:self.button03,
                         4:self.button04,
                         5:self.button05,
                         6:self.button06,
                         7:self.button07,
                         8:self.button08,
                         9:self.button09,
                         10:self.button10,
                         11:self.button11}

        self.buttonNamesDict={1:"Login",
                              2:"Signalling",
                              3:"Mode",
                              4:"Direction",
                              5:"Status",
                              6:"Button 06",
                              7:"Button 07",
                              8:"Button 08",
                              9:"Button 09",
                              10:"Button 10",
                              11:"Button 11"}

    def configureWidgets(self):
        #configuring buttons
        utils.placeGridConfigure(self, 1, 11, 0.003, self)

        for key in self.buttonDict:
            self.buttonDict[key].config(text=self.buttonNamesDict[key],value=key,indicatoron=0,
                          variable=self.radioButtonVar,relief='flat',
                          bg="#FFFFFF",offrelief='flat',command= lambda temp=key: self.displayFrame(temp),font=utils.defaultFont)
        
        

        # print(self.winfo_geometry())

    def placeWidgets(self):
        #Buttons
        utils.placeInGrid(self,self.button01,0,0)
        utils.placeInGrid(self,self.button02,0,1)
        utils.placeInGrid(self,self.button03,0,2)
        utils.placeInGrid(self,self.button04,0,3)
        utils.placeInGrid(self,self.button05,0,4)
        utils.placeInGrid(self,self.button06,0,5)
        utils.placeInGrid(self,self.button07,0,6)
        utils.placeInGrid(self,self.button08,0,7)
        utils.placeInGrid(self,self.button09,0,8)
        utils.placeInGrid(self,self.button10,0,9)
        utils.placeInGrid(self,self.button11,0,10)
        

    def disableButtonsExcept(self,buttonsToBeLeft):         

        for key in self.buttonDict:
            if key not in buttonsToBeLeft:
                self.buttonDict[key].config(state="disabled",text="")
            else:
                self.buttonDict[key].config(state="normal",text=self.buttonNamesDict[key])

    def displayFrame(self,frameIndex):
        for (frame,index) in self.master.frameDict.items():
            if index==frameIndex:
                frame.grid(row=0,column=0,rowspan=self.master.numberOfRows-2,columnspan=self.master.numberOfColumns, padx=2,pady=2,sticky="news")
                self.master.infoFrame.frame_label.config(text=self.master.buttonsFrame.buttonNamesDict[frameIndex])
            else:
                frame.grid_remove()

    def enableAll(self):
        for key in self.buttonDict:
            self.buttonDict[key].config(state="normal",text=self.buttonNamesDict[key])

    radioButtonVar=1
    numberOfColumns=11

class Login(Frame):
    def __init__(self,master,root):
        Frame.__init__(self,master,bg="#000000")
        self.root=root
        # print("creating login frame")
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()

    def createWidgets(self):
        #Frame that contains user label and entry boxes
        self.northFrame=Frame(self,bg="white")

        #User ID label
        self.userIDLabel=Label(self.northFrame,bg="#000000",text="User ID",font=self.font,fg="white",padx=0,pady=0)

        #Entry label
        self.entryLabel=Label(self.northFrame,bg="#000000",text="Entry",font=self.font,fg="white")

        #Valid Label
        self.validLabel=Label(self.northFrame,bg="#000000",text="Valid",font=self.font,fg="white")

        #actual entry box
        self.entryBoxLabel=Label(self.northFrame,bg="#000000",font=self.font,fg="white",padx=0,anchor="w")

        #Validity label
        self.validBoxLabel=Label(self.northFrame,bg="#000000",font=self.font,fg="white")

        #Frame that contains the keypad
        self.keyPadFrame=Frame(self,bg="#000000")

        #keypad Buttons
        self.button1=Button(self.keyPadFrame,text="1")
        self.button2=Button(self.keyPadFrame,text="2")
        self.button3=Button(self.keyPadFrame,text="3")
        self.button4=Button(self.keyPadFrame,text="4")
        self.button5=Button(self.keyPadFrame,text="5")
        self.button6=Button(self.keyPadFrame,text="6")
        self.button7=Button(self.keyPadFrame,text="7")
        self.button8=Button(self.keyPadFrame,text="8")
        self.button9=Button(self.keyPadFrame,text="9")
        self.button0=Button(self.keyPadFrame,text="   0   ")
        self.buttonBack=Button(self.keyPadFrame,text="Back")
        self.buttonEnter=Button(self.keyPadFrame,text="Enter")

        self.keyPadButtonDict={ self.button1:1,
                                self.button2:2,
                                self.button3:3,
                                self.button4:4,
                                self.button5:5,
                                self.button6:6,
                                self.button7:7,
                                self.button8:8,
                                self.button9:9,
                                self.button0:11,
                                self.buttonBack:10,
                                self.buttonEnter:12}

    def configureWidgets(self):
        for button,val in self.keyPadButtonDict.items():
            button.configure(font=self.font,command=lambda val=val:self.buttonPressed(val))

    def placeWidgets(self):
        self.northFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.33)

        self.userIDLabel.place(relx=0.003,rely=0.01,relwidth=0.294,relheight=0.98)
        self.entryLabel.place(relx=0.303,rely=0.01,relwidth=0.344,relheight=0.48)
        self.validLabel.place(relx=0.303,rely=0.51,relwidth=0.344,relheight=0.48)
        self.entryBoxLabel.place(relx=0.653,rely=0.01,relwidth=0.344,relheight=0.48)
        self.validBoxLabel.place(relx=0.653,rely=0.51,relwidth=0.344,relheight=0.48)

        self.keyPadFrame.place(relx=0.5,rely=0.7,relheight=0.4,relwidth=0.3,anchor="center")

        for y in range(4):
            for x in range(3):
                self.getKey(self.loopIndex,self.keyPadButtonDict).place(relheight=0.23,relwidth=(1/3-1/60),rely=((0.23*y)+(0.01)*(2*y+1)),relx=((1/3-1/60)*x)+(1/80)*(x+1))
                self.loopIndex+=1
           
    
    def testGrid(self):
        for x in range(self.numberOfRows):
            for y in range(self.numberOfColumns):
                button=Button(self).grid(row=x,column=y,sticky="news")

    def getStatus(self):
        if 1:
            return "Driver"
        elif 2:
            return "Maintenance"
        elif 3:
            return "Exit"

    def getKey(self,val,myDict):
        for key,value in myDict.items():
            if val==value :
                return key

    def buttonPressed(self,val):

        #Keypad update and login check if enter is pressed
        if val==10:
            self.entryBoxLabel.configure(text=self.entryBoxLabel.cget("text")[:-1])
        elif val==11:
            self.entryBoxLabel.configure(text=self.entryBoxLabel.cget("text")+str(0))
        elif val==12:
            entry_text = self.entryBoxLabel.cget("text")
    
            if entry_text == "123":
                self.root.setState("Driver")
                self.root.buttonsFrame.button03.invoke()
                self.entryBoxLabel.config(text="")
            elif entry_text == "321":
                self.root.setState("Maintenance")
                self.root.buttonsFrame.button02.invoke()
                self.entryBoxLabel.config(text="")
            elif entry_text == "69":
                # self.root.shutDown()
                self.root.stop.set()
                self.root.setState("Exit")
                # self.root.eventControl=False

            elif entry_text == "96":
                self.root.setState("Lock")
                self.entryBoxLabel.config(text="")
            else:
                self.validBoxLabel.configure(text="Invalid")
                self.entryBoxLabel.config(text="")
        else:
            self.entryBoxLabel.configure(text=self.entryBoxLabel.cget("text")+str(val))

        #Realtime entry check and update valid
        if self.entryBoxLabel.cget("text")=="123":
            self.validBoxLabel.configure(text="Driver")
        elif self.entryBoxLabel.cget("text")=="321":
            self.validBoxLabel.configure(text="Maintenance")
        elif self.entryBoxLabel.cget("text")=="69":
            self.validBoxLabel.configure(text="Exit")
        elif self.entryBoxLabel.cget("text")=="96":
            self.validBoxLabel.configure(text="Lock")
        elif val != 12:
            self.validBoxLabel.configure(text="")

    #Variables
    font="Calibri 20"
    numberOfRows=5
    numberOfColumns=7
    entryText=""
    loopIndex=1

class Frame02(Frame):

    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="#000000")
        self.reset=Button(self, text="Reset Signals",command=self.resetSignals,font=utils.defaultFont)
        self.reset.place(relx=0.375,rely=0.375,anchor="center",relheight=0.48,relwidth=0.25)
        self.direction=Button(self, text="Change Directions",command=self.changeDirection,font=utils.defaultFont)
        self.direction.place(relx=0.65,rely=0.375,anchor="center",relheight=0.48,relwidth=0.25)
        self.audio=Button(self, text="Stop Audio",command=self.audio)
        self.audio.place(relx=0.5,rely=0.625,anchor="center",relheight=0.248,relwidth=0.25)
        self.fault=Button(self, text="Train crosses yellow light",command=self.fault,font=utils.defaultFont)
        self.fault.place(relx=0.5,rely=0.875,anchor="center",relheight=0.248,relwidth=0.25)

    
    def resetSignals(self):
        self.root.register.reset()
    
    def changeDirection(self):
        if self.root.register.direction=="F":
            self.root.register.direction="B"
            self.root.register.reset()

            self.root.mux.direction="B"
        elif self.root.register.direction=="B":
            self.root.register.direction="F"
            self.root.register.reset()

            self.root.mux.direction="F"
    
    def fault(self):
        if self.root.register.direction=="F":
            self.root.register.forward=[[1,0,0,0],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
            self.root.register.push()
            
        elif self.root.register.direction=="B":
            self.root.register.backward=[[1,0,1,0],[0,0,1,0],[0,0,0,1],[0,1,0,0]]
            self.root.register.push()

    def audio(self):
        self.root.register.stopAudio()
        print("Stopping Audio")

class Frame03(Frame):

    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="#000000")
        utils.gridConfigure(1,3,self)
        self.createWidgets()
        self.placeWidgets()

    def createWidgets(self):
        self.mode01=Radiobutton(self,text="Drive",variable=self.radioButtonVar,value=0,selectcolor="light Green",indicatoron=0,command=self.driveCommand,font=utils.defaultFont)
        self.mode02=Radiobutton(self,text="Simulate",variable=self.radioButtonVar,value=1,selectcolor="light Green",indicatoron=0,command=self.simCommand,font=utils.defaultFont)
        self.mode03=Radiobutton(self,text="Demo",variable=self.radioButtonVar,value=2,selectcolor="light Green",indicatoron=0,command=self.demoCommand,font=utils.defaultFont)

    def placeWidgets(self):
        self.mode01.grid(row=0,column=0,sticky="news",padx=2,pady=2)
        self.mode02.grid(row=0,column=1,sticky="news",padx=2,pady=2)
        self.mode03.grid(row=0,column=2,sticky="news",padx=2,pady=2)

    def driveCommand(self):
        self.root.infoFrame.modeLabel.config(text="Drive")
        self.root.buttonsFrame.button05.invoke()

    def simCommand(self):
        self.root.infoFrame.modeLabel.config(text="Simulate")
        self.root.buttonsFrame.button05.invoke()

    def demoCommand(self):
        self.root.infoFrame.modeLabel.config(text="Demo")
        self.root.buttonsFrame.button05.invoke()
        
    radioButtonVar=2

class Frame04(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="#000000")
        self.fault=Button(self, text="Change Direction (train)",command=self.fault,font=utils.defaultFont)
        self.fault.place(relx=0.5,rely=0.875,anchor="center",relheight=0.248,relwidth=0.25)

    def fault(self):
        if self.root.dir==1:
            self.root.dir=0
        elif self.root.dir==0:
            self.root.dir=1

        print(self.root.dir)

class Frame05(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="white")
        utils.placeGridConfigure(self,20,20,0.002,self)        
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()


    def createWidgets(self):

        self.beautyFrame=Frame(self,bg="black")

        self.vFrame=Frame(self,bg="#000000")
        self.vLabel=Label(self.vFrame,text="OHE Voltage",bg="#000000",fg="#FFFFFF", font=utils.defaultFont)
        self.vValue=Label(self.vFrame,text="11.87"+"V",bg="#000000",fg="#FFFFFF",font=utils.defaultFont)                
        self.cFrame=Frame(self,bg="#000000")
        self.cLabel=Label(self.cFrame,text="OHE Current",bg="#000000",fg="#FFFFFF",font=utils.defaultFont)
        self.cValue=Label(self.cFrame,text="200 mA",bg="#000000",fg="#FFFFFF",font=utils.defaultFont)

        self.coastFrame=Frame(self,bg="#000000")
        self.coastLabel=Label(self.coastFrame,text="MODE",bg="#000000",fg="#FFFFFF",font=utils.defaultFont )

        self.speedFrame=Frame(self,bg="#000000")
        self.speedLabel=Label(self.speedFrame,text="Speed(km/hr)",bg="#000000",fg="#FFFFFF",font=utils.defaultFont )
        self.speedValue=Label(self.speedFrame,text="0",bg="#000000",fg="#FFFFFF",font=utils.defaultFont)

        self.beautyFrame=Frame(self,bg="#000000")

        self.statusFrame1=Frame(self.beautyFrame,bg='grey')
        self.unit1Label=Label(self.statusFrame1,fg="white",bg="grey",text="Unit 1",font=utils.defaultFont)
        self.subStatus01=SubStatus(self.statusFrame1,self,[utils.blue,
                                                           utils.blue,
                                                           utils.blue,
                                                           utils.white,
                                                           utils.blue,
                                                           utils.blue,
                                                           utils.white,
                                                           utils.blue,
                                                           utils.white,
                                                           utils.blue,
                                                           utils.blue,
                                                           utils.pink
                                                           ])

        self.statusFrame2=Frame(self.beautyFrame,bg='grey')
        self.unit2Label=Label(self.statusFrame2,fg="white",bg="grey",text="Unit 2",font=utils.defaultFont)
        self.subStatus02=SubStatus(self.statusFrame2,self,[utils.blue,
                                                           utils.blue,
                                                           utils.blue,
                                                           utils.white,
                                                           utils.blue,
                                                           utils.blue,
                                                           utils.white,
                                                           utils.blue,
                                                           utils.white,
                                                           utils.blue,
                                                           utils.white,
                                                           utils.pink
                                                           ])
        self.subStatus02.frame11.config(text="")

        self.statusFrame3=Frame(self.beautyFrame,bg='grey')
        self.unit3Label=Label(self.statusFrame3,fg="white",bg="grey",text="Unit 3",font=utils.defaultFont)
        self.subStatus03=SubStatus(self.statusFrame3,self,[utils.blue,
                                                           utils.white,
                                                           utils.blue,
                                                           utils.white,
                                                           utils.blue,
                                                           utils.blue,
                                                           utils.white,
                                                           utils.blue,
                                                           utils.white,
                                                           utils.blue,
                                                           utils.red,
                                                           utils.pink
                                                           ])

       


        

    def configureWidgets(self):
        utils.placeGridConfigure(self,17,20,0.002,self.beautyFrame)
        utils.gridConfigure(10,1,self.statusFrame1)
        utils.gridConfigure(10,1,self.statusFrame2)
        utils.gridConfigure(10,1,self.statusFrame3)

    def placeWidgets(self):


        utils.placeInGrid(self,self.beautyFrame,3,0,17,20)   

        utils.placeInGrid(self,self.vFrame,0,0,columnspan=6,rowspan=3)
        self.vLabel.place(relx=0,rely=0,relheight=0.3,relwidth=0.4,anchor="nw")
        self.vValue.place(relx=0.3,rely=0.4,relheight=0.4,relwidth=0.4,anchor="nw")

        utils.placeInGrid(self,self.cFrame,0,6,columnspan=6,rowspan=3)
        self.cLabel.place(relx=0,rely=0,relheight=0.3,relwidth=0.4,anchor='nw')       
        self.cValue.place(relx=0.3,rely=0.4,relheight=0.4,relwidth=0.4,anchor='nw') 

        utils.placeInGrid(self,self.coastFrame,0,12,columnspan=4,rowspan=3)
        self.coastLabel.place(relx=0,rely=0,relheight=0.3,relwidth=0.4,anchor='nw')

        utils.placeInGrid(self,self.speedFrame,0,16,columnspan=4,rowspan=3)
        self.speedLabel.place(relx=0,rely=0,relheight=0.3,relwidth=0.6,anchor='nw')
        self.speedValue.place(relx=0.3,rely=0.4,relheight=0.4,relwidth=0.4,anchor="nw")


        utils.placeInGrid(self,self.statusFrame1,1,1,12,4)
        self.unit1Label.grid(row=0,column=0,sticky="news")
        self.subStatus01.grid(row=1,column=0,rowspan=9,sticky="news",padx=5,pady=5)

        utils.placeInGrid(self,self.statusFrame2,1,6,12,4)
        self.unit2Label.grid(row=0,column=0,sticky="news")
        self.subStatus02.grid(row=1,column=0,rowspan=9,sticky="news",padx=5,pady=5)

        utils.placeInGrid(self,self.statusFrame3,1,11,12,4)
        self.unit3Label.grid(row=0,column=0,sticky="news")
        self.subStatus03.grid(row=1,column=0,rowspan=9,sticky="news",padx=5,pady=5)    
        
class SubStatus(Frame): 
    def __init__(self,master,root,colourArray):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="#000000")
        utils.placeGridConfigure(self,6,2,0.003,self)
        self.colour=colourArray
        self.images()
        self.createWidgets()
        self.placeWidgets()

    def createWidgets(self):
        self.frame01=Label(self,bg=self.colour[0],text="AC",font=utils.defaultFont)
        self.frame02=Label(self,bg=self.colour[1],text="CAB",font=utils.defaultFont)
        self.frame03=Label(self,bg=self.colour[2],image=self.button03_img,borderwidth=0)
        self.frame04=Label(self,bg=self.colour[3],image=self.button04_img,borderwidth=0)
        self.frame05=Label(self,bg=self.colour[4],image=self.button05_img,borderwidth=0)
        self.frame06=Label(self,bg=self.colour[5],image=self.button06_img,borderwidth=0)
        self.frame07=Label(self,bg=self.colour[6],image=self.button07_img,borderwidth=0)
        self.frame08=Label(self,bg=self.colour[7],image=self.button08_img,borderwidth=0)
        self.frame09=Label(self,bg=self.colour[8],image=self.button09_img,borderwidth=0)
        self.frame10=Label(self,bg=self.colour[9],image=self.button10_img,borderwidth=0)
        self.frame11=Label(self,bg=self.colour[10],text="AWS",font=utils.defaultFont)
        self.frame12=Label(self,bg=self.colour[11],image=self.button12_img,borderwidth=0)
    def placeWidgets(self):
        utils.placeInGrid(self,self.frame01,0,0)
        utils.placeInGrid(self,self.frame02,0,1)
        utils.placeInGrid(self,self.frame03,1,0)
        utils.placeInGrid(self,self.frame04,1,1)
        utils.placeInGrid(self,self.frame05,2,0)
        utils.placeInGrid(self,self.frame06,2,1)
        utils.placeInGrid(self,self.frame07,3,0)
        utils.placeInGrid(self,self.frame08,3,1)
        utils.placeInGrid(self,self.frame09,4,0)
        utils.placeInGrid(self,self.frame10,4,1)
        utils.placeInGrid(self,self.frame11,5,0)
        utils.placeInGrid(self,self.frame12,5,1)

    def images(self):
        self.button03_img=PhotoImage(file=sys.path[0]+"/images/button03.png").subsample(4,4)
        self.button04_img=PhotoImage(file=sys.path[0]+"/images/button04.png").subsample(4,4)
        self.button05_img=PhotoImage(file=sys.path[0]+"/images/button05.png").subsample(4,4)
        self.button06_img=PhotoImage(file=sys.path[0]+"/images/button06.png").subsample(4,4)
        self.button07_img=PhotoImage(file=sys.path[0]+"/images/button07.png").subsample(4,4)
        self.button08_img=PhotoImage(file=sys.path[0]+"/images/button08.png").subsample(4,4)
        self.button09_img=PhotoImage(file=sys.path[0]+"/images/button09.png").subsample(4,4)
        self.button10_img=PhotoImage(file=sys.path[0]+"/images/button10.png").subsample(4,4)
        self.button11_img=PhotoImage(file=sys.path[0]+"/images/button11.png").subsample(4,4)
        self.button12_img=PhotoImage(file=sys.path[0]+"/images/button12.png").subsample(4,4)

class Frame06(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="#000000")

class Frame07(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="#000000")

class Frame08(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="#000000")

class Frame09(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="#000000")

class Frame10(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="#000000")

class Frame11(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="#000000")

class Indicator(Frame):
    def __init__(self,master,root,label,barColor,maxValStr,unitStr):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="#000000")

        utils.placeGridConfigure(self, 12, 12, 0, self)

        self.labelText=label
        self.barColor=barColor
        self.maxVal=maxValStr
        self.unitStr=unitStr
        

        self.createWidgets()
        self.placeWidgets()
        

    def createWidgets(self):
        self.mainLabel=Label(self,bg="#000000",text=self.labelText,font=utils.defaultFont,fg="white",anchor="center")
        self.maxLabel=Label(self,bg="#000000",text=str(self.maxVal),font=utils.defaultFont,fg="white")
        self.unitLabel=Label(self,bg="#000000",text=self.unitStr,font=utils.defaultFont,fg="white")

        self.canvas=Canvas(master=self,bg="#000000",border=0)
        utils.placeInGrid(self,self.canvas,5,1,6,10)

        self.rect=Frame(self.canvas,bg=self.barColor)

        
        self.bar=self.canvas.create_window(utils.returnCoord(self,self.canvas,0,0.25),window=self.rect,width=self.canvas.winfo_width(),anchor="nw")

        self.createCanvas()
        

    def placeWidgets(self):
        utils.placeInGrid(self,self.mainLabel,0,0,4,4)
        utils.placeInGrid(self,self.maxLabel,0,10,2,2)
        utils.placeInGrid(self,self.unitLabel,2,10,2,2)





    def createCanvas(self):
        self.canvas.update()
        l1=self.canvas.create_line(utils.rectCoord(self,self.canvas,0.001,0,1,0),fill="white",width=3,state=DISABLED)
        l2=self.canvas.create_line(utils.rectCoord(self,self.canvas,0.1,0.2,0.6,0),fill="grey",width=3,state=DISABLED)
        l3=self.canvas.create_line(utils.rectCoord(self,self.canvas,0.2,0,1,0),fill="white",width=3,state=DISABLED)
        l4=self.canvas.create_line(utils.rectCoord(self,self.canvas,0.3,0.2,0.6,0),fill="grey",width=3,state=DISABLED)
        l5=self.canvas.create_line(utils.rectCoord(self,self.canvas,0.4,0,1,0),fill="white",width=3,state=DISABLED)
        l6=self.canvas.create_line(utils.rectCoord(self,self.canvas,0.5,0.2,0.6,0),fill="grey",width=3,state=DISABLED)
        l7=self.canvas.create_line(utils.rectCoord(self,self.canvas,0.6,0,1,0),fill="white",width=3,state=DISABLED)
        l8=self.canvas.create_line(utils.rectCoord(self,self.canvas,0.7,0.2,0.6,0),fill="grey",width=3,state=DISABLED)
        l9=self.canvas.create_line(utils.rectCoord(self,self.canvas,0.8,0,1,0),fill="white",width=3,state=DISABLED)
        l10=self.canvas.create_line(utils.rectCoord(self,self.canvas,0.9,0.2,0.6,0),fill="grey",width=3,state=DISABLED)
        l11=self.canvas.create_line(utils.rectCoord(self,self.canvas,0.999,0,1,0),fill="white",width=3,state=DISABLED)


    def updateWidth(self,val):
        self.rect.place(relx=0,rely=0.25,relheight=0.5,relwidth=(val/self.maxVal))

    

        

        

