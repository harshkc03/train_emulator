from tkinter import*

#MainWindow Class
class MainWIndow(Tk):
    def __init__(self,master=None):
        Tk.__init__(self,master)
        self.geometry('1200x675')
        self.config(bg="#000000")
        self.rowconfigure(1,minsize=60)
        self.createWidgets()
        self.placeWidgets()
        self.initialiseWidgets()    
    
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



                 
    def placeWidgets(self):
        #Top Level Frame
        self.topLevelFrame.grid(sticky=self.stickyValue,row=2,column=0,columnspan=11,padx=5,pady=5,rowspan=11)

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
        self.frame01.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())
        self.frame02.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())
        self.frame03.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())
        self.frame04.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())
        self.frame05.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())
        self.frame06.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())
        self.frame07.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())
        self.frame08.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())
        self.frame09.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())
        self.frame10.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())
        self.frame11.config(height=self.topLevelFrame.winfo_height(),width=self.topLevelFrame.winfo_width())

        self.update()        
        self.testWidgetGeometry()

    def initialiseWidgets(self):
        print("Initialising.....")

    def testWidgetGeometry(self):
        print("Button 1")
        print(self.button01.winfo_geometry())
        print('\n')
        print("Button 2")
        print(self.button02.winfo_geometry())
        print('\n')
        print("Button 3")
        print(self.button03.winfo_geometry())
        print('\n')
        print("Button 4")
        print(self.button04.winfo_geometry())
        print('\n')
        print("Button 5")
        print(self.button05.winfo_geometry())
        print('\n')
        print("Button 6")
        print(self.button06.winfo_geometry())
        print('\n')
        print("Button 7")
        print(self.button07.winfo_geometry())
        print('\n')
        print("Button 8")
        print(self.button08.winfo_geometry())
        print('\n')
        print("Button 9")
        print(self.button09.winfo_geometry())
        print('\n')
        print("Button 10")
        print(self.button10.winfo_geometry())
        print('\n')
        print("Button 11")
        print(self.button11.winfo_geometry())
        print('\n')
        print("Top level frame")
        print(self.topLevelFrame.winfo_geometry())
        print('\n')
        print("MainWindow")
        print(self.winfo_geometry())                
       
    #Button Functions
    def button01Func(self):
        print("Button 1 is pressed")
        self.frame01.grid(sticky=self.stickyValue,padx=2,pady=2)
        self.frame02.grid_remove()
        self.frame03.grid_remove()
        self.frame04.grid_remove()
        self.frame05.grid_remove()
        self.frame06.grid_remove()
        self.frame07.grid_remove()
        self.frame08.grid_remove()
        self.frame09.grid_remove()
        self.frame10.grid_remove()
        self.frame11.grid_remove() 
        self.testWidgetGeometry()
                    
    def button02Func(self):
        print("Button 2 is pressed")
        self.frame01.grid_remove()
        self.frame02.grid(sticky=self.stickyValue,padx=2,pady=2)
        self.frame03.grid_remove()
        self.frame04.grid_remove()
        self.frame05.grid_remove()
        self.frame06.grid_remove()
        self.frame07.grid_remove()
        self.frame08.grid_remove()
        self.frame09.grid_remove()
        self.frame10.grid_remove()
        self.frame11.grid_remove() 
        self.testWidgetGeometry()
        
    def button03Func(self):
        print("Button 3 is pressed")
        self.frame01.grid_remove()
        self.frame02.grid_remove()
        self.frame03.grid(sticky=self.stickyValue,padx=2,pady=2)
        self.frame04.grid_remove()
        self.frame05.grid_remove()
        self.frame06.grid_remove()
        self.frame07.grid_remove()
        self.frame08.grid_remove()
        self.frame09.grid_remove()
        self.frame10.grid_remove()
        self.frame11.grid_remove() 
        self.testWidgetGeometry()

    def button04Func(self):
        print("Button 4 is pressed")
        self.frame01.grid_remove()
        self.frame02.grid_remove()
        self.frame03.grid_remove()
        self.frame04.grid(sticky=self.stickyValue,padx=2,pady=2)
        self.frame05.grid_remove()
        self.frame06.grid_remove()
        self.frame07.grid_remove()
        self.frame08.grid_remove()
        self.frame09.grid_remove()
        self.frame10.grid_remove()
        self.frame11.grid_remove() 
        self.testWidgetGeometry()

    def button05Func(self):
        print("Button 5 is pressed")
        self.frame01.grid_remove()
        self.frame02.grid_remove()
        self.frame03.grid_remove()
        self.frame04.grid_remove()
        self.frame05.grid(sticky=self.stickyValue,padx=2,pady=2)
        self.frame06.grid_remove()
        self.frame07.grid_remove()
        self.frame08.grid_remove()
        self.frame09.grid_remove()
        self.frame10.grid_remove()
        self.frame11.grid_remove() 
        self.testWidgetGeometry()

    def button06Func(self):
        print("Button 6 is pressed")
        self.frame01.grid_remove()
        self.frame02.grid_remove()
        self.frame03.grid_remove()
        self.frame04.grid_remove()        
        self.frame05.grid_remove()
        self.frame06.grid(sticky=self.stickyValue,padx=2,pady=2)
        self.frame07.grid_remove()
        self.frame08.grid_remove()
        self.frame09.grid_remove()
        self.frame10.grid_remove()
        self.frame11.grid_remove() 
        self.testWidgetGeometry()
        
    def button07Func(self):
        print("Button 7 is pressed")
        self.frame01.grid_remove()
        self.frame02.grid_remove()
        self.frame03.grid_remove()
        self.frame04.grid_remove()        
        self.frame05.grid_remove()
        self.frame06.grid_remove()
        self.frame07.grid(sticky=self.stickyValue,padx=2,pady=2)        
        self.frame08.grid_remove()
        self.frame09.grid_remove()
        self.frame10.grid_remove()
        self.frame11.grid_remove() 
        self.testWidgetGeometry()

    def button08Func(self):
        print("Button 8 is pressed")
        self.frame01.grid_remove()
        self.frame02.grid_remove()
        self.frame03.grid_remove()
        self.frame04.grid_remove()        
        self.frame05.grid_remove()
        self.frame06.grid_remove()                
        self.frame07.grid_remove()
        self.frame08.grid(sticky=self.stickyValue,padx=2,pady=2)
        self.frame09.grid_remove()
        self.frame10.grid_remove()
        self.frame11.grid_remove() 
        self.testWidgetGeometry()

    def button09Func(self):
        print("Button 9 is pressed")
        self.frame01.grid_remove()
        self.frame02.grid_remove()
        self.frame03.grid_remove()
        self.frame04.grid_remove()        
        self.frame05.grid_remove()
        self.frame06.grid_remove()
        self.frame07.grid_remove()       
        self.frame08.grid_remove()
        self.frame09.grid(sticky=self.stickyValue,padx=2,pady=2)
        self.frame10.grid_remove()
        self.frame11.grid_remove() 
        self.testWidgetGeometry()

    def button10Func(self):
        print("Button 10 is pressed")
        self.frame01.grid_remove()
        self.frame02.grid_remove()
        self.frame03.grid_remove()
        self.frame04.grid_remove()        
        self.frame05.grid_remove()
        self.frame06.grid_remove()                
        self.frame08.grid_remove()
        self.frame09.grid_remove()
        self.frame10.grid(sticky=self.stickyValue,padx=2,pady=2)
        self.frame11.grid_remove() 
        self.testWidgetGeometry()

    def button11Func(self):
        print("Button 11 is pressed")
        self.frame01.grid_remove()
        self.frame02.grid_remove()
        self.frame03.grid_remove()
        self.frame04.grid_remove()        
        self.frame05.grid_remove()
        self.frame06.grid_remove()   
        self.frame07.grid_remove()            
        self.frame08.grid_remove()
        self.frame09.grid_remove()
        self.frame10.grid_remove()        
        self.frame11.grid(sticky=self.stickyValue,padx=2,pady=2) 
        self.testWidgetGeometry()

    
    #Variables
    mainRadioButtonVariable=1
    stickyValue="news"
    topLevelFrameHeight=900
    

app=MainWIndow()
app.mainloop()
        
