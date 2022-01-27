from tkinter import *
from child_frames import *



class MainWindow:
    def __init__(self):
        root=Tk()
        root.geometry('800x70')
        root.config(bg="green")
        self.gridConfigure(self.numberOfRows,self.numberOfColumns,root)

        self.frame=buttonFrame.ButtonHolder(root)
        self.frame.grid(row=0,column=0,sticky="news")       

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
    

