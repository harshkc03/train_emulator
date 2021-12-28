from tkinter import*

#MainWindow Class
class MainWIndow(Tk):
    def __init__(self,master=None):
        Tk.__init__(self,master)
        self.geometry('1920x1080')
        self.config(bg="#000000")
        self.rowconfigure(1,minsize=60)
        self.createWidgets()
        self.placeWidgets()

    
    def createWidgets(self):
        #RadioButtons
        self.button01=Radiobutton(self,variable=self.mainRadioButtonVariable,indicatoron=0,text="Test Button 1",relief='fla')
        self.button02=Radiobutton(self,variable=self.mainRadioButtonVariable,indicatoron=0,text="Test Button 2")
        self.button03=Radiobutton(self,variable=self.mainRadioButtonVariable,indicatoron=0,text="Text Button 3")
        self.button04=Radiobutton(self,variable=self.mainRadioButtonVariable,indicatoron=0,text="Text Button 4")
        self.button05=Radiobutton(self,variable=self.mainRadioButtonVariable,indicatoron=0,text="Text Button 5")
        self.button06=Radiobutton(self,variable=self.mainRadioButtonVariable,indicatoron=0,text="Text Button 6")
        self.button07=Radiobutton(self,variable=self.mainRadioButtonVariable,indicatoron=0,text="Text Button 7")
        self.button08=Radiobutton(self,variable=self.mainRadioButtonVariable,indicatoron=0,text="Text Button 8")
        self.button09=Radiobutton(self,variable=self.mainRadioButtonVariable,indicatoron=0,text="Text Button 9")
        self.button10=Radiobutton(self,variable=self.mainRadioButtonVariable,indicatoron=0,text="Text Button 10")
        self.button11=Radiobutton(self,variable=self.mainRadioButtonVariable,indicatoron=0,text="Text Button 11")
        
        #Usable Frames
        self.infoFrame=Frame(self,bg="#000000")

        #Fillers
        self.filler01=Label(text="Filler 01")
        self.filler02=Label(text="Filler 02")
        self.filler03=Label(text="Filler 03")

        #Filler Frames
        self.frame01=Frame(self,bg="#000000")
        self.frame02=Frame(self,bg="#000000")
        self.frame03=Frame(self,bg="#000000")
        self.frame04=Frame(self,bg="#000000")
        self.frame05=Frame(self,bg="#000000")


    
    def placeWidgets(self):
        #info Frame
        self.infoFrame.grid(row=0,rowspan=1,column=0,columnspan=11)
        
        #Buttons
        self.button01.grid(sticky=self.stickyValue,row=1,column=0,padx=5)
        self.button02.grid(sticky=self.stickyValue,row=1,column=1,padx=5)
        self.button03.grid(sticky=self.stickyValue,row=1,column=2,padx=5)
        self.button04.grid(sticky=self.stickyValue,row=1,column=3,padx=5)
        self.button05.grid(sticky=self.stickyValue,row=1,column=4,padx=5)
        self.button06.grid(sticky=self.stickyValue,row=1,column=5,padx=5)
        self.button07.grid(sticky=self.stickyValue,row=1,column=6,padx=5)
        self.button08.grid(sticky=self.stickyValue,row=1,column=7,padx=5)
        self.button09.grid(sticky=self.stickyValue,row=1,column=8,padx=5)
        self.button10.grid(sticky=self.stickyValue,row=1,column=9,padx=5)
        self.button11.grid(sticky=self.stickyValue,row=1,column=10,padx=5)
              
        
        #Update geometry and configure the widgets
        self.update()
        self.configureWidgets()    

    def configureWidgets(self):
        #Frames
        self.infoFrame.config(width=self.winfo_width(),height=self.button01.winfo_height())

        #Buttons
        

        #Filler Frames
        self.frame01.config(width=self.button03.winfo_width(),height=self.button03.winfo_height())
        self.frame02.config(width=self.button03.winfo_width(),height=self.button03.winfo_height())
        self.frame03.config(width=self.button03.winfo_width(),height=self.button03.winfo_height())
        self.frame04.config(width=self.button03.winfo_width(),height=self.button03.winfo_height())
        self.frame05.config(width=self.button03.winfo_width(),height=self.button03.winfo_height())

    #Variables
    mainRadioButtonVariable=1
    stickyValue="news"

app=MainWIndow()
app.mainloop()
        
