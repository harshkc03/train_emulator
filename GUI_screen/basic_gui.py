from tkinter import *
  
  
# create root window
MainWindow = Tk()            

  
# frame inside root window
frame = Frame(MainWindow, borderwidth=5)  
              
  
# geometry method
frame.pack()                          
  
# button inside frame which is 
# inside root
button = Button(frame, text ='CONTROLS',background='black',foreground='white',activebackground='black',activeforeground='white')  
button.pack()                         
  
# Tkinter event loop
MainWindow.mainloop()   