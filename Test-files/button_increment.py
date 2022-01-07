from tkinter import * 

class GUI_handle():

	def __init__(self):

		#MainWindow
		self.MainWindow = Tk()
		self.MainWindow.geometry('500x500')

		#Variables for use
		self.my_Var = 0

		#Label
		self.label = Label(self.MainWindow, text=str(self.my_Var), borderwidth=5)
		self.label.place(x=10,y=80,height=50,width=100)

		#Button
		self.button = Button(self.MainWindow, text ='DIE!',background='black',foreground='white',
						activebackground='black',activeforeground='white', command=self.changeValue)  
		self.button.place(x=10,y=10,height=50,width=100) 

		# Tkinter event loop
		self.MainWindow.mainloop() 
	
	#Functions for use
	def changeValue(self):

		self.my_Var+=1

		#Update text
		self.label.configure(text = str(self.my_Var))

gui = GUI_handle()