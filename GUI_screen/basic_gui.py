from tkinter import * 

#Variables for use
my_Var = 0

#MainWindow
MainWindow = Tk()
MainWindow.geometry('500x500')
    
#Label
label=Label(MainWindow,text=str(my_Var),borderwidth=5,)
label.place(x=10,y=80,height=50,width=100)

#Functions for use
def changeValue():

    global my_Var
    my_Var+=1

    #Update text
    label.configure(text = str(my_Var))

#Button
button = Button(MainWindow, text ='DIE!',background='black',foreground='white',
                activebackground='black',activeforeground='white', command=changeValue)  
button.place(x=10,y=10,height=50,width=100) 

# Tkinter event loop
MainWindow.mainloop()   