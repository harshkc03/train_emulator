from tkinter import * 

class GUI_Parent:
    #Constructor
    def __init__(self):
        #Variables 
        self.my_var=0

        #MainWindow
        self.MainWindow=Tk()
        self.MainWindow.attributes("-fullscreen",True)

        ##GUI Components

        #Increment_Button        
        self.incrementButton=Button(self.MainWindow,text='+1',background='black',foreground='white',
                                    activeforeground='white',activebackground='dark blue',command=self.incValue)
        self.incrementButton.place(x=10,y=10,height=40,width=100)

        #Decrement_Button
        self.decrementButton=Button(self.MainWindow,text='-1',background='black',foreground='white',
                                    activeforeground='white',activebackground='dark blue',command=self.decValue)
        self.decrementButton.place(x=120,y=10,height=40,width=100)

        #Close_Button
        self.closeButton=Button(self.MainWindow,text='Close',background='red',foreground='black',command=self.MainWindow.destroy)
        self.closeButton.place(x=230,y=10,height=40,width=200)

        #Label
        self.textLabel=Label(self.MainWindow,text=self.my_var,borderwidth=5)
        self.textLabel.place(x=10,y=60,height=40,width=200)

    #Functions
    def incValue(self):
        self.my_var+=1
        self.textLabel.configure(text=self.my_var)

    def decValue(self):
        if self.my_var!=0:
            self.my_var-=1
        self.textLabel.configure(text=self.my_var)


guiObject=GUI_Parent()
guiObject.MainWindow.mainloop() 