from tkinter import *

class GUI_Parent:
    #Constructor
    def __init__(self):
        
        #Variables 
        self.my_var=0

        #MainWindow
        self.MainWindow=Tk()
        

        

        ##GUI Components

        #Increment_Button        
        self.incrementButton=Button(self.MainWindow,text='+1',background='black',foreground='white',
                                    activeforeground='white',activebackground='gray14',command=self.incValue)
        self.incrementButton.place(x=10,y=10,height=40,width=100)

        #Decrement_Button
        self.decrementButton=Button(self.MainWindow,text='-1',background='black',foreground='white',
                                    activeforeground='white',activebackground='gray14',command=self.decValue)
        self.decrementButton.place(x=120,y=10,height=40,width=100)

        #Close_Button
        self.closeButton=Button(self.MainWindow,text='Close',background='red',foreground='black',activebackground='pink',command=self.MainWindow.destroy)
        self.closeButton.place(x=230,y=10,height=40,width=200)

        #Label
        self.textLabel=Label(self.MainWindow,text=self.my_var,borderwidth=5,background='blue',foreground='yellow')
        self.textLabel.place(x=10,y=60,height=40,width=200)

        #Username_Label
        self.usernameLabel=Label(self.MainWindow,text='Username:')
        self.usernameLabel.place(x=440,y=10,width=100,height=40)

        #Username_Entry
        self.usernameEntry=Entry(self.MainWindow)
        self.usernameEntry.place(x=550,y=15,width=200,height=30)

        #Password_Label
        self.passwordLabel=Label(self.MainWindow,text='Password:')
        self.passwordLabel.place(x=440,y=60,width=100,height=40)

        #Password_Entry
        self.passwordEntry=Entry(self.MainWindow)
        self.passwordEntry.place(x=550,y=65,width=200,height=30)

        

        #RadioButtons
        self.radioButton1=Radiobutton(self.MainWindow,text='Menu 1',variable=1,value=1,
                                      indicator=0).place(x=760,y=10,width=100,height=40)
        self.radioButton2=Radiobutton(self.MainWindow,text='Menu 2',variable=1,value=2,
                                      indicator=0).place(x=760,y=50,width=100,height=40)
        self.radioButton3=Radiobutton(self.MainWindow,text='Menu 3',variable=1,value=3,
                                      indicator=0).place(x=760,y=90,width=100,height=40)
        self.radioButton4=Radiobutton(self.MainWindow,text='Menu 4',variable=1,value=4,
                                      indicator=0).place(x=760,y=130,width=100,height=40)

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