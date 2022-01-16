from tkinter import Radiobutton, Frame
import common_functions

class ButtonHolder(Frame):
    def __init__(self,master):
        Frame.__init__(self,master,bg="black")
        common_functions.gridConfigure(1,11,self)
        self.createWidgets()
        self.configureWidgets()
        self.placeWidgets()

    def createWidgets(self):
        #Buttons
        self.button01=Radiobutton(self)
        self.button02=Radiobutton(self)
        self.button03=Radiobutton(self)
        self.button04=Radiobutton(self)
        self.button05=Radiobutton(self)
        self.button06=Radiobutton(self)
        self.button07=Radiobutton(self)
        self.button08=Radiobutton(self)
        self.button09=Radiobutton(self)
        self.button10=Radiobutton(self)
        self.button11=Radiobutton(self)

        #Dictionary containing buttons and an index
        self.buttonDict={self.button01:1,
                         self.button02:2,
                         self.button03:3,
                         self.button04:4,
                         self.button05:5,
                         self.button06:6,
                         self.button07:7,
                         self.button08:8,
                         self.button09:9,
                         self.button10:10,
                         self.button11:11}

        self.buttonNamesDict={1:"Login",
                              2:"button02",
                              3:"Mode",
                              4:"Button 04",
                              5:"Button 05",
                              6:"Button 06",
                              7:"Button 07",
                              8:"Button 08",
                              9:"Button 09",
                              10:"Button 10",
                              11:"Button 11"}

    def configureWidgets(self):
        #configuring buttons
        for button,index in self.buttonDict.items():
            button.config(text=self.buttonNamesDict[index],value=index,indicatoron=0,
                          variable=self.radioButtonVar,relief='flat',
                          bg="#FFFFFF",offrelief='flat')

    def placeWidgets(self):
        #Buttons
        for button,index in self.buttonDict.items():
            button.grid(row=0,column=index-1,sticky="news",padx=2)

    def disableButtonsExcept(self,buttonsToBeLeft):         

        for button in self.buttonDict:
            if self.buttonDict[button] not in buttonsToBeLeft:
                button.config(state="disabled",text="")
            else:
                button.config(state="normal",text=self.buttonNamesDict[self.buttonDict[button]])

    radioButtonVar=1
