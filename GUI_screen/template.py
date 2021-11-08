from tkinter import *
import datetime

class GUI_parent:

    def __init__(self):
        #MainWindow
        self.MainWindow=Tk()
        # self.MainWindow.attributes("-fullscreen",True)
        # self.MainWindow.size = (1366,768)
        self.MainWindow.geometry("1366x768")
        self.MainWindow.configure(background='black')

        #Close_Button
        self.closeButton=Button(self.MainWindow,text='Exit',background='red',foreground='white',command=self.MainWindow.destroy)
        self.closeButton.place(relx=0.5, rely=0.8, width=100, height=30, anchor=CENTER)

        self.header = Canvas(self.MainWindow, bg="black",
           height=40, width=1320, highlightthickness=3)

        self.train_no_rect = self.header.create_rectangle(0, 0, 325, 50, outline="white", width=4)
        self.train_no = self.header.create_text((162, 22), text="Train: 69145", fill="white", font=("lucida", 15))

        self.window_name="Login User ID"
        self.window_name_rect = self.header.create_rectangle(325, 0, 995, 50, outline="white", width=4)
        self.window_name_text = self.header.create_text((660, 22), text=self.window_name, fill="white", font=("lucida", 15))

        self.date = str(datetime.datetime.today().strftime('%m/%d/%Y'))
        self.date_rect = self.header.create_rectangle(995, 0, 1165, 50, outline="white", width=4)
        self.date_text = self.header.create_text((1080, 22), text=self.date, fill="white", font=("lucida", 15))

        self.time = str(datetime.datetime.now().strftime("%H:%M:%S"))
        # self.time_rect = self.header.create_rectangle(995, 0, 1165, 50, outline="white", width=4)
        self.time_text = self.header.create_text((1250, 22), text=self.time, fill="white", font=("lucida", 15))

        self.header.place(relx=0.5, rely=0.045, anchor=CENTER)
        self.cur_clock()
    
    def cur_clock(self):
        self.time = str(datetime.datetime.now().strftime("%H:%M:%S"))
        self.header.itemconfig(self.time_text, text=self.time)
        self.MainWindow.after(1000,self.cur_clock)

guiObject=GUI_parent()
guiObject.cur_clock()
guiObject.MainWindow.after(0,guiObject.cur_clock)
guiObject.MainWindow.mainloop() 