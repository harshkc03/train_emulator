import login_screen
from tkinter import *

class MainWindow:
    def __init__(self):
        root=Tk()
        root.geometry('450x450')
        root.config(bg="#000000")
        self.gridConfigure(self.numberOfRows,self.numberOfColumns,root)
        
        self.frame01=login_screen.Login(root,root)    
        self.frame01.grid(sticky="news")

        root.mainloop()

    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1,minsize=(root.winfo_height()/rows))
        for x in range(columns):
            root.columnconfigure(x,weight=1,minsize=(root.winfo_width()/columns))
        
    numberOfRows=1
    numberOfColumns=1

app=MainWindow()
    

