from tkinter import * 

#Variables for use
my_Var = 0

#MainWindow
MainWindow = Tk()
MainWindow.geometry('500x500')

#Button
button = Button(MainWindow, text ='DIE!',background='black',foreground='white',
                activebackground='black',activeforeground='white', command=MainWindow.destroy)  
button.place(x=10,y=10,height=50,width=100) 

#Button Command
def changeValue():
    global my_Var
    my_Var+=1

  
# Tkinter event loop
MainWindow.mainloop()   