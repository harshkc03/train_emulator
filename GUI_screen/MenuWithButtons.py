from tkinter import *
from typing import Mapping

class TheContainerClass:
    #Constructor
    def __init__(self):
        #Main_Window
        self.MainWindow=Tk()
        self.MainWindow.geometry('500x500')

        #Windows/Frames
        self.loginFrame=Frame(self.MainWindow)
        self.loginFrame.configure(bg='black')
        self.mainFrame=Frame(self.MainWindow)
        self.mainFrame.configure(background='black')
        self.menu1=Frame(self.mainFrame)
        self.menu2=Frame(self.mainFrame)
        self.menu3=Frame(self.mainFrame)

        #LoginFrame_Widgets
        self.usernameLabel=Label(self.loginFrame)
        self.usernameLabel.configure(text='Username: ')
        self.passwordLabel=Label(self.loginFrame)
        self.passwordLabel.configure(text='Password: ')
        
        #Frame1_Widgets
        self.label1=Label(self.menu1)
        self.label1.configure(text='I am from menu 1',justify=LEFT,background='black',foreground='white')
        self.label1.place(x=10,y=10,height=40,width=300)

        #Frame2_Widgets
        self.label2=Label(self.menu2)
        self.label2.configure(text='I am from menu 2',justify=LEFT,background='green',foreground='white')
        self.label2.place(x=10,y=70,height=40,width=300)

        #Frame3_Widgets
        self.label3=Label(self.menu3)
        self.label3.configure(text='I am Menu3 da launda',justify=RIGHT,background='blue',foreground='white')
        self.label3.place(x=10,y=110,height=40,width=300)


        #Frame_Control_Buttons
        self.menuButton1=Radiobutton(text='Menu 1',variable=9999,value=1,indicatoron=False,command=self.menuButton1Clicked)
        self.menuButton2=Radiobutton(text='Menu 2',variable=9999,value=2,indicatoron=False,command=self.menuButton2Clicked)
        self.menuButton3=Radiobutton(text='Menu 3',variable=9999,value=3,indicatoron=False,command=self.menuButton3Clicked)
        self.menuButton1.select()

        #Packing
        self.mainFrame.pack(fill=BOTH,expand=True)
        self.menu1.pack(fill=BOTH,expand=True)
        self.menuButton1.pack(side=LEFT,fill=X,expand=True,ipady=5)
        self.menuButton2.pack(side=LEFT,fill=X,expand=True,ipady=5)
        self.menuButton3.pack(side=LEFT,fill=X,expand=True,ipady=5)

     #Functions
    def menuButton1Clicked(self):
         self.menu1.pack(fill=BOTH,expand=True)
         self.menu2.pack_forget()
         self.menu3.pack_forget()

    def menuButton2Clicked(self):
         self.menu1.pack_forget()
         self.menu2.pack(fill=BOTH,expand=True)
         self.menu3.pack_forget()

    def menuButton3Clicked(self):
         self.menu1.pack_forget()
         self.menu2.pack_forget()
         self.menu3.pack(fill=BOTH,expand=True)

        

gui=TheContainerClass()
gui.MainWindow.mainloop()     