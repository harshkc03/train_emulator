import login_screen
from tkinter import *

class MainWindow:
    def __init__(self):
        root=Tk()
        root.geometry('450x450')
        self.gridConfigure(self.numberOfRows,self.numberOfColumns,root)
        
        self.frame01=login_screen.Login(root)    
        self.frame01.grid(row=1,column=1,sticky="news")

        root.mainloop()

    def gridConfigure(self,rows,columns,frame):
        for x in range(rows):
            frame.rowconfigure(x,weight=1)
        for x in range(columns):
            frame.columnconfigure(x,weight=1)
        
    
    numberOfRows=3
    numberOfColumns=3

app=MainWindow()
    

