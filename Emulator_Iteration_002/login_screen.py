import collections
from tkinter import*
from tkinter import font

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
           
    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1,minsize=(root.winfo_height()/rows))
        for x in range(columns):
            root.columnconfigure(x,weight=1,minsize=(root.winfo_width()/columns))

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
                self.root.button03.invoke()
            elif entry_text == "321":
                self.root.setState("Maintenance")
                self.root.button02.invoke()
            elif entry_text == "69":
                self.root.setState("Exit")
            elif entry_text == "96":
                self.root.disableButtonsExcept([1])
            else:
                self.validBoxLabel.configure(text="Invalid")
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
    