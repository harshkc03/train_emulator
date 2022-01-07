# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from os import name
from pathlib import Path
from tkinter import *

class login_frame(Frame):
    
    def __init__(self, window, root):
        Frame.__init__(self, window)

        self.MainWindow = root
        self.frame_name = "Login"

        self.user_text = StringVar(self,"")

        OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = OUTPUT_PATH / Path("./assets")

        self.createLoginCanvas()
        self.createKeypad()

        # Disable all the Radiobuttons except the login one
        for (button,buttonIndex) in self.MainWindow.buttonArray.items():
            if buttonIndex != 1:
                button.config(state='disabled')
    
    def createLoginCanvas(self):

        canvas = Canvas(
            self,
            bg = "#000000",
            height = 590,
            width = 1267,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            317.0,
            61.0,
            950.0,
            202.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            321.0,
            64.0,
            946.0,
            199.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            541.0,
            130.0,
            745.0,
            198.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            745.0,
            131.0,
            945.0,
            198.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            745.0,
            65.0,
            945.0,
            133.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            541.0,
            65.0,
            745.0,
            133.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            545.0,
            133.0,
            741.0,
            194.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            545.0,
            69.0,
            741.0,
            130.0,
            fill="#000000",
            outline="")

        canvas.create_rectangle(
            745.0,
            133.0,
            941.0,
            194.0,
            fill="#000000",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            843.0,
            99.5,
            image=self.entry_image_1
        )

        self.entry_text_id = canvas.create_text(
            757.0,
            88.0,
            anchor="nw",
            text="",
            fill="#FFFFFF",
            font=("Roboto", 24 * -1)
        )

        canvas.create_text(
            390.0,
            121.0,
            anchor="nw",
            text="User ID",
            fill="#FFFFFF",
            font=("Roboto", 24 * -1)
        )

        canvas.create_text(
            558.0,
            88.0,
            anchor="nw",
            text="Entry",
            fill="#FFFFFF",
            font=("Roboto", 24 * -1)
        )

        canvas.create_text(
            558.0,
            152.0,
            anchor="nw",
            text="Valid",
            fill="#FFFFFF",
            font=("Roboto", 24 * -1)
        )

        self.valid_text_id = canvas.create_text(
            757.0,
            152.0,
            anchor="nw",
            text="",
            fill="#FFFFFF",
            font=("Roboto", 24 * -1)
        )

        canvas.create_rectangle(
            451.0,
            255.0,
            816.0,
            504.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_rectangle(
            454.0,
            258.0,
            813.0,
            501.0,
            fill="#000000",
            outline="")
        
        self.canvas = canvas

    def createKeypad(self):

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_1 clicked"),
            command=lambda val="1":self.keypadEntry(val),
            relief="flat"
        )
        button_1.place(
            x=455.0,
            y=259.0,
            width=117.0,
            height=58.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_3 clicked"),
            command=lambda val="3":self.keypadEntry(val),
            relief="flat"
        )
        button_2.place(
            x=695.0,
            y=259.0,
            width=117.0,
            height=58.0
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_2 clicked"),
            command=lambda val="2":self.keypadEntry(val),
            relief="flat"
        )
        button_3.place(
            x=575.0,
            y=259.0,
            width=117.0,
            height=58.0
        )

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_back-space clicked"),
            command=lambda val="-1":self.keypadEntry(val),
            relief="flat"
        )
        button_4.place(
            x=455.0,
            y=442.0,
            width=117.0,
            height=58.0
        )

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_enter clicked"),
            command= self.loginCheck,
            relief="flat"
        )
        button_5.place(
            x=695.0,
            y=442.0,
            width=117.0,
            height=58.0
        )

        self.button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_0 clicked"),
            command=lambda val="0":self.keypadEntry(val),
            relief="flat"
        )
        button_6.place(
            x=575.0,
            y=442.0,
            width=117.0,
            height=58.0
        )

        self.button_image_7 = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        button_7 = Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_7 clicked"),
            command=lambda val="7":self.keypadEntry(val),
            relief="flat"
        )
        button_7.place(
            x=455.0,
            y=381.0,
            width=117.0,
            height=58.0
        )

        self.button_image_8 = PhotoImage(
            file=self.relative_to_assets("button_8.png"))
        button_8 = Button(
            self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_9 clicked"),
            command=lambda val="9":self.keypadEntry(val),
            relief="flat"
        )
        button_8.place(
            x=695.0,
            y=381.0,
            width=117.0,
            height=58.0
        )

        self.button_image_9 = PhotoImage(
            file=self.relative_to_assets("button_9.png"))
        button_9 = Button(
            self,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_8 clicked"),
            command=lambda val="8":self.keypadEntry(val),
            relief="flat"
        )
        button_9.place(
            x=575.0,
            y=381.0,
            width=117.0,
            height=58.0
        )

        self.button_image_10 = PhotoImage(
            file=self.relative_to_assets("button_10.png"))
        button_10 = Button(
            self,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_4 clicked"),
            command=lambda val="4":self.keypadEntry(val),
            relief="flat"
        )
        button_10.place(
            x=455.0,
            y=320.0,
            width=117.0,
            height=58.0
        )

        self.button_image_11 = PhotoImage(
            file=self.relative_to_assets("button_11.png"))
        button_11 = Button(
            self,
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_6 clicked"),
            command=lambda val="6":self.keypadEntry(val),
            relief="flat"
        )
        button_11.place(
            x=695.0,
            y=320.0,
            width=117.0,
            height=58.0
        )

        self.button_image_12 = PhotoImage(
            file=self.relative_to_assets("button_12.png"))
        button_12 = Button(
            self,
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            # command=lambda: print("button_5 clicked"),
            command=lambda val="5":self.keypadEntry(val),
            relief="flat"
        )
        button_12.place(
            x=575.0,
            y=320.0,
            width=117.0,
            height=58.0
        )
    
    def keypadEntry(self, num):

        if num == "-1":
            self.user_text.set(self.user_text.get()[:-1])
        else:
            self.user_text.set(self.user_text.get() + num)

        entry = self.user_text.get()

        self.canvas.itemconfig(self.entry_text_id, text=entry)

        if entry == '123':
            self.canvas.itemconfig(self.valid_text_id, text="Driver")
        elif entry == '96':
            self.canvas.itemconfig(self.valid_text_id, text="Lock")
        elif entry == '69':
            self.canvas.itemconfig(self.valid_text_id, text="Exit")
        else:
            self.canvas.itemconfig(self.valid_text_id, text="")

    def loginCheck(self):
        entry = self.user_text.get()

        if entry == "69":
            exit(0)
        elif entry == "123":
            for (button,buttonIndex) in self.MainWindow.buttonArray.items():
                if buttonIndex != 1:
                    button.config(text="Text Button "+str(buttonIndex),state='normal')
            self.MainWindow.button02.invoke()
        elif entry == "96":
            for (button,buttonIndex) in self.MainWindow.buttonArray.items():
                if buttonIndex != 1:
                    button.config(text="",state='disabled')
        else:
            self.canvas.itemconfig(self.valid_text_id, text="INVALID")

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

        
