from tkinter import *

class Login:

    #Initializer
    def __init__(self,master):
        self.fancyFrame=Frame(master,bg="white",height=500,width=800)
        self.userFrame=Frame(self.fancyFrame,bg="#000000",height=490,width=790).grid(in_=self.fancyFrame)
        self.userLabel=Label(self.userFrame,text="User",bg="#000000",font="15",fg="White").grid(in_=self.userFrame)
        
        
        