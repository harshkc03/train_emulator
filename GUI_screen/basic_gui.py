from tkinter import *
  
  
# create root window
MainWindow = Tk()

MainWindow.geometry('500x500')

button = Button(MainWindow, text ='DIE!',background='black',foreground='white',activebackground='black',activeforeground='white', command=MainWindow.destroy)  

button.place(x=10,y=10,height=50,width=100)                         
  
# Tkinter event loop
MainWindow.mainloop()   