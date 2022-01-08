import login_screen
from tkinter import *

class MainWindow:
    def __init__(self):
        root=Tk()
        root.geometry('450x450')
        root.config(bg="#000000")
        self.gridConfigure(self.numberOfRows,self.numberOfColumns,root)

        self.button01=Radiobutton(text="Button 01",indicatoron=0,variable=1,value=1,selectcolor="light green")
        self.button02=Radiobutton(text="Button 02",indicatoron=0,variable=1,value=2,selectcolor="light green")
        self.button03=Radiobutton(text="Button 03",indicatoron=0,variable=1,value=3,selectcolor="light green")

        self.button01.grid(row=0,column=0,sticky="news")
        self.button02.grid(row=0,column=1,sticky="news")
        self.button03.grid(row=0,column=2,sticky="news")

       

        root.mainloop()

    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1,minsize=(root.winfo_height()/rows))
        for x in range(columns):
            root.columnconfigure(x,weight=1,minsize=(root.winfo_width()/columns))
        
    numberOfRows=1
    numberOfColumns=3

app=MainWindow()
    

