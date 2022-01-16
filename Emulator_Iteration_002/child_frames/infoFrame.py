from tkinter import*
import datetime

class InfoFrame(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,bg="white")
        self.gridConfigure(1,11,self)
        self.createWidgets()
        self.placeWidgets()
        self.initTime()

    def createWidgets(self):
        #Info Frame Children
        self.trainNoFrame=Frame(self,bg="#000000")
        self.train_label=Label(self.trainNoFrame,text="Train: 69145",bg="#000000",fg="white",font=self.defaultFont)

        self.titleFrame=Frame(self,bg="#000000")
        self.frame_label=Label(self.titleFrame,text="",bg="#000000",fg="white",font=self.defaultFont)

        self.modeFrame=Frame(self,bg="#000000")
        self.modeLabel=Label(self.modeFrame,text="Select mode!",bg="#000000",fg="white",font=self.defaultFont)

        self.dateFrame=Frame(self,bg="#000000")
        self.date_label=Label(self.dateFrame,text=str(datetime.datetime.today().strftime('%d/%m/%Y')),bg="#000000",fg="white",font=self.defaultFont)

        self.timeFrame=Frame(self,bg="#000000")      
        self.time_label=Label(self.timeFrame,text=str(datetime.datetime.now().strftime("%H:%M:%S")),bg="#000000",fg="white",font=self.defaultFont)
        
    def placeWidgets(self):
        
        #info Frame Children
        self.trainNoFrame.grid(row=0,column=0,columnspan=2,padx=2,pady=2,sticky="news")
        self.titleFrame.grid(row=0,column=2,columnspan=3,padx=2,pady=2,sticky="news")
        self.modeFrame.grid(row=0,column=5,columnspan=2,padx=2,pady=2,sticky="news")
        self.dateFrame.grid(row=0,column=7,columnspan=2,padx=2,pady=2,sticky="news")
        self.timeFrame.grid(row=0,column=9,columnspan=2,padx=2,pady=2,sticky="news")

        self.train_label.place(anchor=CENTER,relx=0.5,rely=0.5)
        self.frame_label.place(anchor=CENTER,relx=0.5,rely=0.5)
        self.date_label.place(anchor=CENTER,relx=0.5,rely=0.5)
        self.time_label.place(anchor=CENTER,relx=0.5,rely=0.5)
        self.modeLabel.place(anchor=CENTER,relx=0.5,rely=0.5)

    def gridConfigure(self,rows,columns,root):
        root.update()
        for x in range(rows):
            root.rowconfigure(x,weight=1,minsize=(root.winfo_height()/rows))
        for x in range(columns):
            root.columnconfigure(x,weight=1,minsize=(root.winfo_width()/columns))

    def initTime(self):
        self.after(0, self.update_clock)

    def update_clock(self):
        self.time_label.config(text=str(datetime.datetime.now().strftime("%H:%M:%S")))
        self.after(1000, self.update_clock)

    defaultFont="Calibri 15"
    