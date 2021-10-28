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
        self.buttonWidget=Widget(self.MainWindow,widgetName='buttons')

        #Array_of_Buttons
        self.driveButton=Button(self.buttonWidget, text='Drive/Brake',background='white',foreground='black')
        self.driveButton.grid(row=0,column=0)        
        self.airButton=Button(self.buttonWidget,text='Air Spring', background='white', foreground='black')
        self.airButton.grid(row=0,column=1)
        self.energyButton=Button(self.buttonWidget,text='EnergyOver', background='white', foreground='black')
        self.energyButton.grid(row=0,column=2) 
        self.brakeButton=Button(self.buttonWidget,text='Brake', background='white', foreground='black')
        self.brakeButton.grid(row=0,column=3)
        self.loginButton=Button(self.buttonWidget,text='Login', background='white', foreground='black')
        self.loginButton.grid(row=0,column=4)
        self.eventButton=Button(self.buttonWidget,text='Events', background='white', foreground='black')
        self.eventButton.grid(row=0,column=5)
        self.msgButton=Button(self.buttonWidget,text='Drv Msgs', background='white', foreground='black')
        self.msgButton.grid(row=0,column=6)
        self.maintenanceButton=Button(self.buttonWidget,text='Mainten. Mode', background='white', foreground='black')
        self.maintenanceButton.grid(row=0,column=7)
        self.legendsButton=Button(self.buttonWidget,text='Legends', background='white', foreground='black')
        self.legendsButton.grid(row=0,column=8)
        self.brightButton=Button(self.buttonWidget,text='Brightness', background='white', foreground='black')
        self.driveButton.grid(row=0,column=9)
        self.dummyButton=Button(self.buttonWidget, background='white', foreground='black')
        self.dummyButton.grid(row=0,column=10)

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

guiObject=GUI_parent()
guiObject.cur_clock()
guiObject.MainWindow.mainloop() 