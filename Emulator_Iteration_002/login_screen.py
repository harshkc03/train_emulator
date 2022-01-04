from tkinter import*

class Login(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,bg="blue")
        self.gridConfigure(5,5,self)
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()

    def createWidgets(self):
        #Upper Area
        self.entryFrame=Frame(self,bg="#000000")

        #empty frame for boundary effect
        self.entryDecorFrame=Label(self.entryFrame,bg="white")

        #labels
        self.userLabel=Label(self.entryFrame,text="User ID",bg="#000000",fg="white",font=str(self.fontSize))
        self.entryLabel=Label(self.entryFrame,bg="#000000",text="Entry",fg="white",font=str(self.fontSize))
        self.validLabel=Label(self.entryFrame,text="Valid",bg="#000000",fg="white",font=str(self.fontSize))

        #Text Entry boxes
        self.entryEntry=Entry(self.entryFrame,bg="#000000",fg="white",font=str(self.fontSize))
        self.validEntry=Entry(self.entryFrame,text="Valid",bg="#000000",fg="white",font=str(self.fontSize))

        #empty frame for boundary
        self.keyDecorFrame=Frame(self,bg="#000000")

        #Keypad Container
        self.keyFrame=Frame(self.keyDecorFrame,bg="#000000")

        #Keys in on the keypad
        self.button1=Button(self.keyFrame,bg="white",text="1")
        self.button2=Button(self.keyFrame,bg="white",text="2")
        self.button3=Button(self.keyFrame,bg="white",text="3")
        self.button4=Button(self.keyFrame,bg="white",text="4")
        self.button5=Button(self.keyFrame,bg="white",text="5")
        self.button6=Button(self.keyFrame,bg="white",text="6")
        self.button7=Button(self.keyFrame,bg="white",text="7")
        self.button8=Button(self.keyFrame,bg="white",text="8")
        self.button9=Button(self.keyFrame,bg="white",text="9")
        self.buttonBackspace=Button(self.keyFrame,bg="white",text="Backspace")
        self.button0=Button(self.keyFrame,bg="white",text="0")
        self.buttonEnter=Button(self.keyFrame,bg="white",text="Enter")
        


        

        

    def configureWidgets(self):
        self.gridConfigure(2,5,self.entryFrame)
        self.gridConfigure(1,5,self.keyDecorFrame)
        self.gridConfigure(4,3,self.keyFrame)

    def placeWidgets(self):

        self.entryFrame.grid(row=0,rowspan=2,column=1,columnspan=3,sticky="news")
        self.entryDecorFrame.grid(row=0,column=1,rowspan=2,columnspan=3,sticky="news")

        self.userLabel.grid(row=0,column=1,rowspan=2,padx=4,sticky="news",pady=2)
        self.entryLabel.grid(row=0,column=2,sticky="news",padx=4,pady=2)
        self.validLabel.grid(row=1,column=2,sticky="news",padx=4,pady=2)

        self.entryEntry.grid(row=0,column=3,sticky="news",padx=4,pady=2)
        self.validEntry.grid(row=1,column=3,sticky="news",padx=4,pady=2)

        self.keyDecorFrame.grid(row=2,rowspan=3,column=1,columnspan=3,sticky="news")
        self.keyFrame.grid(columnspan=3,column=1,sticky="news")

        self.button1.grid(row=0,column=0,sticky="news",padx=2,pady=2)
        self.button2.grid(row=0,column=1,sticky="news",padx=2,pady=2)
        self.button3.grid(row=0,column=2,sticky="news",padx=2,pady=2)
        self.button4.grid(row=1,column=0,sticky="news",padx=2,pady=2)
        self.button5.grid(row=1,column=1,sticky="news",padx=2,pady=2)
        self.button6.grid(row=1,column=2,sticky="news",padx=2,pady=2)
        self.button7.grid(row=2,column=0,sticky="news",padx=2,pady=2)
        self.button8.grid(row=2,column=1,sticky="news",padx=2,pady=2)
        self.button9.grid(row=2,column=2,sticky="news",padx=2,pady=2)
        self.buttonBackspace.grid(row=3,column=0,sticky="news",padx=2,pady=2)
        self.button0.grid(row=3,column=1,sticky="news",padx=2,pady=2)
        self.buttonEnter.grid(row=3,column=2,sticky="news",padx=2,pady=2)
        
        

    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1)
        for x in range(columns):
            root.columnconfigure(x,weight=1)

    #Variables
    fontSize=50
    