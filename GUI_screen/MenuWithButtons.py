from tkinter import *
from typing import Mapping

class TheContainerClass:
    #Constructor
    def __init__(self):
        #Main_Window
        self.MainWindow=Tk()
        self.MainWindow.geometry('500x500')

        #Windows/Frames
        self.mainFrame=Frame(self.MainWindow)
        self.mainFrame.configure(background='black')
        self.menu1=Frame(self.mainFrame)
        self.menu2=Frame(self.mainFrame)
        
        #Frame1_Widgets
        self.label1=Label(self.menu1)
        self.label1.configure(text='I am from menu 1',justify=LEFT,background='black',foreground='white')
        self.label1.place(x=10,y=10,height=40,width=300)

        #Frame_Control_Buttons
        self.menuButton1=Radiobutton(text='Menu 1',variable=9999,value=1,indicatoron=False,command=self.menuButton1Clicked)
        self.menuButton2=Radiobutton(text='Menu 2',variable=9999,value=2,indicatoron=False,command=self.menuButton2Clicked)
        self.menuButton1.select()

        #Packing
        self.mainFrame.pack(fill=BOTH,expand=True)
        self.menu1.pack(fill=BOTH,expand=True)
        self.menuButton1.pack(side=LEFT,fill=X,expand=True,ipady=5)
        self.menuButton2.pack(side=LEFT,fill=X,expand=True,ipady=5)

     #Functions
    def menuButton1Clicked(self):
         self.menu1.pack(fill=BOTH,expand=True)
         self.menu2.pack_forget()

    def menuButton2Clicked(self):
         self.menu1.pack_forget()
         self.menu2.pack(fill=BOTH,expand=True)

        

gui=TheContainerClass()
gui.MainWindow.mainloop()
        
        

        