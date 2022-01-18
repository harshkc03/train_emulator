from tkinter import *
import datetime
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
        utils.gridConfigure(1,11,self)
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()

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

        self.buttonNamesDict={1:"Login",
                              2:"button02",
                              3:"Mode",
                              4:"Button 04",
                              5:"Button 05",
                              6:"Button 06",
                              7:"Button 07",
                              8:"Button 08",
                              9:"Button 09",
                              10:"Button 10",
                              11:"Button 11"}

    def configureWidgets(self):
        #configuring buttons
        for button,index in self.buttonDict.items():
            button.config(text=self.buttonNamesDict[index],value=index,indicatoron=0,
                          variable=self.radioButtonVar,relief='flat',
                          bg="#FFFFFF",offrelief='flat',command= lambda temp=index: self.displayFrame(temp))

    def placeWidgets(self):
        #Buttons
        for button,index in self.buttonDict.items():
            button.grid(row=0,column=index-1,sticky="news",padx=2)

    def disableButtonsExcept(self,buttonsToBeLeft):         

        for button in self.buttonDict:
            if self.buttonDict[button] not in buttonsToBeLeft:
                button.config(state="disabled",text="")
            else:
                button.config(state="normal",text=self.buttonNamesDict[self.buttonDict[button]])

    def displayFrame(self,frameIndex):
        for (frame,index) in self.master.frameDict.items():
            if index==frameIndex:
                frame.grid(row=0,column=0,rowspan=self.master.numberOfRows-2,columnspan=self.master.numberOfColumns, padx=2,pady=2,sticky="news")
                self.master.infoFrame.frame_label.config(text=self.master.buttonsFrame.buttonNamesDict[frameIndex])
            else:
                frame.grid_remove()

    def enableAll(self):
        for button in self.buttonDict:
            button.config(state="normal",text=self.buttonNamesDict[self.buttonDict[button]])

    radioButtonVar=1
    numberOfColumns=11

class Login(Frame):
    def __init__(self,master,root):
        Frame.__init__(self,master,bg="#000000")
        self.root=root
        print("creating login frame")
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
                self.root.setState("Exit")
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
        Frame.__init__(self,master,bg="red")
        
class Frame03(Frame):

    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="pink")
        utils.gridConfigure(1,3,self)
        self.createWidgets()

        self.placeWidgets()

    def createWidgets(self):
        self.mode01=Radiobutton(self,text="Drive",variable=self.radioButtonVar,value=0,selectcolor="light Green",indicatoron=0,command=lambda temp="Drive":self.modeCommand(temp))
        self.mode02=Radiobutton(self,text="Simulate",variable=self.radioButtonVar,value=1,selectcolor="light Green",indicatoron=0,command=lambda temp="Simulate":self.modeCommand(temp))
        self.mode03=Radiobutton(self,text="Demo",variable=self.radioButtonVar,value=2,selectcolor="light Green",indicatoron=0,command=lambda temp="Demo":self.modeCommand(temp))

    def placeWidgets(self):
        self.mode01.grid(row=0,column=0,sticky="news",padx=2,pady=2)
        self.mode02.grid(row=0,column=1,sticky="news",padx=2,pady=2)
        self.mode03.grid(row=0,column=2,sticky="news",padx=2,pady=2)

    def modeCommand(self,label):
        self.root.infoFrame.modeLabel.config(text=label)
        self.root.buttonsFrame.button05.invoke()
        
    radioButtonVar=2

class Frame04(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="pink")

class Frame05(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="pink")

class Frame06(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="pink")

class Frame07(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="pink")

class Frame08(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="pink")

class Frame09(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="pink")

class Frame10(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="pink")

class Frame11(Frame):
    def __init__(self,master,root):
        self.root=root
        self.master=master
        Frame.__init__(self,master,bg="pink")

