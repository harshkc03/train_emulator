from tkinter import *
import sys


mainWindow = Tk()

mainWindow.geometry('1200x800')

button03_image=PhotoImage(file=sys.path[0]+"/images/button03.png").subsample(3,3)
button04_image=PhotoImage(file=sys.path[0]+"/images/button04.png").subsample(3,3)
button05_image=PhotoImage(file=sys.path[0]+"/images/button05.png").subsample(3,3)
button06_image=PhotoImage(file=sys.path[0]+"/images/button06.png").subsample(3,3)
button07_image=PhotoImage(file=sys.path[0]+"/images/button07.png").subsample(3,3)
button08_image=PhotoImage(file=sys.path[0]+"/images/button08.png").subsample(3,3)
button09_image=PhotoImage(file=sys.path[0]+"/images/button09.png").subsample(3,3)
button10_image=PhotoImage(file=sys.path[0]+"/images/button10.png").subsample(3,3)
button11_image=PhotoImage(file=sys.path[0]+"/images/button11.png").subsample(3,3)
button12_image=PhotoImage(file=sys.path[0]+"/images/button12.png").subsample(3,3)

button01=Button(mainWindow, text="AC")
button02=Button(mainWindow, text="CAB")
button03=Button(mainWindow, image=button03_image)
button04=Button(mainWindow, image=button04_image)
button05=Button(mainWindow, image=button05_image)
button06=Button(mainWindow, image=button06_image)
button07=Button(mainWindow, image=button07_image)
button08=Button(mainWindow, image=button08_image)
button09=Button(mainWindow, image=button09_image)
button10=Button(mainWindow, image=button10_image)
button11=Button(mainWindow, image=button11_image)
button12=Button(mainWindow, image=button12_image)

button03.grid(row=0, column=0,sticky=N+S+E+W)
button04.grid(row=0, column=1,sticky=N+S+E+W)
button05.grid(row=1, column=0,sticky=N+S+E+W)
button06.grid(row=1, column=1,sticky=N+S+E+W)
button07.grid(row=2, column=0,sticky=N+S+E+W)
button08.grid(row=2, column=1,sticky=N+S+E+W)
button09.grid(row=3, column=0,sticky=N+S+E+W)
button10.grid(row=3, column=1,sticky=N+S+E+W)
button11.grid(row=4, column=0,sticky=N+S+E+W)
button12.grid(row=4, column=1,sticky=N+S+E+W)


mainWindow.mainloop()

