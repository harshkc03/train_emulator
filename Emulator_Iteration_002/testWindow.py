import login_screen
from tkinter import *
from Custom_Classes import custom_frame

class MainWindow:
    def __init__(self):
        root=Tk()
        root.geometry('450x450')
        root.config(bg="green")
        self.gridConfigure(self.numberOfRows,self.numberOfColumns,root)

        self.frame=custom_frame.CustomFrame(root)
        self.frame.config(bg="#000000")
        self.frame.grid(sticky="news")



        self.button01=Button(self.frame)
        self.frame.placeInGrid(self.button01,1,1)

        self.button02=Button(self.frame)
        self.frame.placeInGrid(self.button02,0,2)

        self.button03=Button(self.frame)
        self.frame.placeInGrid(self.button03,0,0)

       

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
    

