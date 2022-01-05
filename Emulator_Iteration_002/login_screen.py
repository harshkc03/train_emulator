import collections
from tkinter import*
from tkinter import font

class Login(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,bg="#000000")
        self.gridConfigure(self.numberOfRows,self.numberOfColumns,self)
        print("creating login frame")
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()

    def createWidgets(self):
        #Frame that contains user label and entry boxes
        self.northFrame=Frame(self,bg="white")

        #User ID label
        self.userIDLabel=Label(self.northFrame,bg="#000000",text="User ID",font=self.font,fg="white")

        #Entry label
        self.entryLabel=Label(self.northFrame,bg="#000000",text="Entry",font=self.font,fg="white")

        #Valid Label
        self.validLabel=Label(self.northFrame,bg="#000000",text="Valid",font=self.font,fg="white")

        #actual entry box
        self.entryBoxLabel=Label(self.northFrame,bg="#000000",font=self.font,fg="white")

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
        self.gridConfigure(2,3,self.northFrame)
        self.gridConfigure(4,3,self.keyPadFrame)

    def placeWidgets(self):
        self.northFrame.grid(row=0,column=0,rowspan=2,columnspan=7,sticky="news",pady=5)

        self.userIDLabel.grid(row=0,column=0,rowspan=2,sticky="news",padx=2,pady=2)
        self.entryLabel.grid(row=0,column=1,sticky="news",padx=2,pady=2)
        self.validLabel.grid(row=1,column=1,sticky="news",padx=2,pady=2)
        self.entryBoxLabel.grid(row=0,column=2,sticky="news",padx=2,pady=2)
        self.validBoxLabel.grid(row=1,column=2,sticky="news",padx=2,pady=2)

        self.keyPadFrame.grid(row=2,rowspan=3,column=2,columnspan=3,sticky="news")

        for x in range(4):
            for y in range(3):
                self.getKey(self.loopIndex,self.keyPadButtonDict).grid(row=x,column=y,sticky="news",padx=2,pady=2)
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


    #Variables
    font="Calibri 20"
    numberOfRows=5
    numberOfColumns=7
    entryText=""
    loopIndex=1
    