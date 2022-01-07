from tkinter import *


class GUI_Parent:
    #Constructor
    def __init__(self):
        
        #Variables 
        self.my_var=0

        #MainWindow
        self.MainWindow=Tk()
        self.MainWindow.attributes("-fullscreen",True)
        self.MainWindow.configure(background='black')

        #Login variables
        self.username = StringVar()
        self.password = StringVar()
        self.message = StringVar()

        ##GUI Components
        #Close_Button
        self.closeButton=Button(self.MainWindow,text='Exit',background='red',foreground='white',command=self.MainWindow.destroy)
        self.closeButton.place(relx=0.5, rely=0.8, width=100, height=30, anchor=CENTER)

        #Username_Label
        self.usernameLabel=Label(self.MainWindow,text='Username:',bg='black',fg='white')
        self.usernameLabel.place(relx=0.4, rely=0.4, width=100, height=30, anchor=CENTER)

        #Username_Entry
        self.usernameEntry=Entry(self.MainWindow, textvariable=self.username)
        self.usernameEntry.place(relx=0.5, rely=0.4, width=200, height=30, anchor=CENTER)

        #Password_Label
        self.passwordLabel=Label(self.MainWindow,text='Password:',bg='black',fg='white')
        self.passwordLabel.place(relx=0.4, rely=0.47, width=100, height=30, anchor=CENTER)

        #Password_Entry
        self.passwordEntry=Entry(self.MainWindow, textvariable=self.password, show='*')
        self.passwordEntry.place(relx=0.5, rely=0.47, width=200, height=30, anchor=CENTER)

        #Login button
        self.login_button = Button(self.MainWindow, text="Login", width=10, height=1, bg=self.rgbtohex(77,68,203), fg='white',command=self.login)
        self.login_button.place(relx=0.5, rely=0.6, width=150, height=30, anchor=CENTER)

        #Login info label
        self.login_info = Label(self.MainWindow, text="",textvariable=self.message,bg='black',fg='white')
        self.login_info.place(relx=0.5, rely=0.52, anchor=CENTER)

    #Functions
    def login(self):

        #getting form data
        uname=self.username.get()
        pwd=self.password.get()

        #applying empty validation
        if uname=='' or pwd=='':
            self.message.set("Username or Password not filled")
        else:
            if uname=="abc" and pwd=="abc":
                self.message.set("Login success")
            else:
                self.message.set("Wrong username or password!!!")
    
    def rgbtohex(self, r,g,b):
        return f'#{r:02x}{g:02x}{b:02x}'


guiObject=GUI_Parent()
guiObject.MainWindow.mainloop() 