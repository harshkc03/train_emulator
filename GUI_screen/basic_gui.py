from tkinter import * 

class GUI_Parent:
    #Constructor
    def _init_(self):
        #Variables 
        self.my_var=0

        #MainWindow
        self.MainWindow=Tk()
        self.MainWindow.geometry('500x500')

        #GUI Components
        self.incrementButton=Button(self.MainWindow,text='+1',background='black',foreground='white',
                                    activeforeground='white',activebackground='dark blue',command=self.changeValue)
        self.incrementButton.place(x=10,y=10,height=40,width=200)

        self.textLabel=Label(self.MainWindow,text=self.my_var,borderwidth=5)
        self.textLabel.place(x=10,y=60,height=40,width=200)

    #Functions
    def changeValue(self):
        self.my_var+=1
        self.textLabel.configure(text=self.my_Var)

guiObject=GUI_Parent()
guiObject.MainWindow.mainloop() 