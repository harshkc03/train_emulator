
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

window = Tk()

window.geometry("1280x720")
window.configure(bg = "#1D1D1D")

#Login variables
username = StringVar()
password = StringVar()
message = StringVar()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


canvas = Canvas(
    window,
    bg = "#1D1D1D",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    48.0,
    40.0,
    1229.0,
    674.0,
    fill="#000000",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png")
)
entry_bg_1 = canvas.create_image(
    640.0,
    298.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=username
)
entry_1.place(
    x=529.0,
    y=278.0,
    width=222.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png")
)
entry_bg_2 = canvas.create_image(
    640.0,
    389.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    textvariable=password
)
entry_2.place(
    x=529.0,
    y=369.0,
    width=222.0,
    height=38.0
)

canvas.create_text(
    518.0,
    256.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("Roboto Medium", 19 * -1)
)

canvas.create_text(
    518.0,
    347.0,
    anchor="nw",
    text="Password",
    fill="#FFFFFF",
    font=("Roboto Medium", 19 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))



login_id = canvas.create_text(
    518.0,
    420.0,
    anchor="nw",
    text="",
    fill="#FFFFFF",
    font=("Roboto Medium", 17 * -1)
)

def login():

    global username, password, message

    #getting form data
    uname=username.get()
    pwd=password.get()

    #applying empty validation
    if uname=='' or pwd=='':
        # message.set("Username or Password not filled")
        canvas.itemconfig(login_id, text="Username or Password not filled")
    else:
        if uname=="abc" and pwd=="abc":
            # message.set("Login success")
            canvas.itemconfig(login_id, text="Login success")
        else:
            # message.set("Wrong username or password!!!")
            canvas.itemconfig(login_id, text="Wrong username or password!!!")

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_1.place(
    x=550.0,
    y=450.0,
    width=181.0,
    height=40.0
)
window.resizable(False, False)
# window.mainloop()