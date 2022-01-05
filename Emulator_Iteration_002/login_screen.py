from tkinter import*

class Login(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,bg="blue")
        self.gridConfigure(self.numberOfRows,self.numberOfColumns,self)
        self.testGrid()

       
    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1,minsize=(root.winfo_height()/rows))
        for x in range(columns):
            root.columnconfigure(x,weight=1,minsize=(root.winfo_width()/columns))

    def testGrid(self):
        for x in range(self.numberOfRows):
            for y in range(self.numberOfColumns):
                button=Button(self).grid(row=x,column=y,sticky="news")


    #Variables
    fontSize=50
    numberOfRows=5
    numberOfColumns=5
    