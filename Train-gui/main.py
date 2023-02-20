from tkinter import *
import threading
import time

import background.gui
import login.gui


class MainWindow(Tk):

    # Constructor
    def __init__(self, window):

        # Initialize this class as the main Tk window
        Tk.__init__(self, window)

        # Set a few parameters for our main window
        self.geometry("1920x1080")
        self.configure(bg = "#000000") # Pitch black background
        self.resizable(False, False)
        self.attributes("-fullscreen", True)

        # Create a thread for performing background tasks
        self.task = threading.Thread(target=self.run_commands, daemon=True)
        self.task.start()

        # Create the main frame with all the buttons
        self.main_frame = background.gui.emu_gui(self)
        self.main_frame.pack(fill=BOTH, expand=True)

        # Create the login frame
        self.login_frame = login.gui.login_gui(self)

        # Timepass frame
        self.fun = funFrame(self)
        self.mode_select = modeFrame(self)
        self.overview = overviewFrame(self)
        self.recreate = recreateFrame(self)
        self.train_pos = trainposFrame(self)
        self.camera = cameraFrame(self)
        self.events = eventsFrame(self)
        self.auto_mode = autoFrame(self)
        self.legends = legendFrame(self)
        self.brightness = brightnessFrame(self)
        self.backlight = backlightFrame(self)

        # Activate the login frame
        self.button1pressed()
        self.change_button_text(1, "Log in")

        # Assign the command functions to the Radiobuttons
        self.main_frame.button_list[0].config(command=self.button1pressed)
        self.main_frame.button_list[1].config(command=self.button2pressed)
        self.main_frame.button_list[2].config(command=self.button3pressed)
        self.main_frame.button_list[3].config(command=self.button4pressed)
        self.main_frame.button_list[4].config(command=self.button5pressed)
        self.main_frame.button_list[5].config(command=self.button6pressed)
        self.main_frame.button_list[6].config(command=self.button7pressed)
        self.main_frame.button_list[7].config(command=self.button8pressed)
        self.main_frame.button_list[8].config(command=self.button9pressed)
        self.main_frame.button_list[9].config(command=self.button10pressed)
        self.main_frame.button_list[10].config(command=self.button11pressed)

        # Disable all the Radiobuttons except the login one
        for i in range(1, 11):
            self.main_frame.button_list[i].configure(state=DISABLED)

    # Function associated with the background thread
    def run_commands(self):

        while True:
            pass
    
    # Function to change the text of a Radiobutton
    def change_button_text(self, number, text):
        self.main_frame.button_list[number-1].config(text=text)

    # Function to track what's being entered in the entry box and display relevant text if the entry matches
    # This is linked with the variable trace command in button1pressed()
    def login_entry_check(self, *args):

        if self.login_frame.entry_text.get() == "696969":
            self.login_frame.canvas.itemconfig(self.login_frame.valid_text_id, text="Exit")
        elif self.login_frame.entry_text.get() == "888888":
            self.login_frame.canvas.itemconfig(self.login_frame.valid_text_id, text="Driver")
        else:
            self.login_frame.canvas.itemconfig(self.login_frame.valid_text_id, text="")

        return True

    # Function to check login credentials
    def login_callback(self):

        # Get the entered text
        entry = self.login_frame.entry_text.get()

        # A highly exclusive ID for the developers of this program (code will directly exit if this ID is entered)
        if entry == "696969":
            self.destroy()
        
        # ID for normal usage of this program
        elif entry == "888888":

            # Remove the variable trace (to save system resources by an infinitesimal amount)
            self.login_frame.entry_text.trace_remove(*self.login_frame.entry_text.trace_info()[0])
            self.login_frame.entry_text.set("")

            # Enable all the Radiobuttons
            for i in range(1, 11):
                self.main_frame.button_list[i].configure(state=NORMAL)

            # Change the text of all the enabled Radiobuttons
            self.change_button_text(2, "Mode")
            self.change_button_text(3, "Overview")
            self.change_button_text(4, "Recreate")
            self.change_button_text(5, "Position")
            self.change_button_text(6, "Camera")
            self.change_button_text(7, "Events")
            self.change_button_text(8, "Auto-run")
            self.change_button_text(9, "Legends")
            self.change_button_text(10, "Brightness")
            self.change_button_text(11, "Backlight")

            # Select button 2 and call the function associated with it
            self.main_frame.button_2.select()
            self.button2pressed()
    
    def button1pressed(self):
        print("button1 pressed")

        # Forget all other frames
        self.mode_select.place_forget()
        self.overview.place_forget()
        self.recreate.place_forget()
        self.train_pos.place_forget()
        self.camera.place_forget()
        self.events.place_forget()
        self.auto_mode.place_forget()
        self.legends.place_forget()
        self.brightness.place_forget()
        self.backlight.place_forget()

        # Bring forward the login frame
        self.login_frame.place(x=18.0, y=204.0, width=1883.0, height=860.0)
        # Create a trace for the entry box text
        self.login_frame.entry_text.trace_add("write", self.login_entry_check)
        self.login_frame.button_1.config(command=self.login_callback)

    def button2pressed(self):
        print("button2 pressed")

        # Forget all other frames
        self.login_frame.place_forget()
        self.overview.place_forget()
        self.recreate.place_forget()
        self.train_pos.place_forget()
        self.camera.place_forget()
        self.events.place_forget()
        self.auto_mode.place_forget()
        self.legends.place_forget()
        self.brightness.place_forget()
        self.backlight.place_forget()

        # Slap the fun frame on top of the main frame
        self.mode_select.place(x=18.0, y=204.0, width=1883.0, height=860.0)

    def button3pressed(self):
        print("button3 pressed")

        self.login_frame.place_forget()
        self.mode_select.place_forget()
        self.recreate.place_forget()
        self.train_pos.place_forget()
        self.camera.place_forget()
        self.events.place_forget()
        self.auto_mode.place_forget()
        self.legends.place_forget()
        self.brightness.place_forget()
        self.backlight.place_forget()

        self.overview.place(x=18.0, y=204.0, width=1883.0, height=860.0)

    def button4pressed(self):
        print("button4 pressed")

        self.login_frame.place_forget()
        self.mode_select.place_forget()
        self.overview.place_forget()
        # self.recreate.place_forget()
        self.train_pos.place_forget()
        self.camera.place_forget()
        self.events.place_forget()
        self.auto_mode.place_forget()
        self.legends.place_forget()
        self.brightness.place_forget()
        self.backlight.place_forget()

        self.recreate.place(x=18.0, y=204.0, width=1883.0, height=860.0)


    def button5pressed(self):
        print("button5 pressed")
        self.login_frame.place_forget()
        self.mode_select.place_forget()
        self.overview.place_forget()
        self.recreate.place_forget()
        # self.train_pos.place_forget()
        self.camera.place_forget()
        self.events.place_forget()
        self.auto_mode.place_forget()
        self.legends.place_forget()
        self.brightness.place_forget()
        self.backlight.place_forget()

        self.train_pos.place(x=18.0, y=204.0, width=1883.0, height=860.0)

    def button6pressed(self):
        print("button6 pressed")
        self.login_frame.place_forget()
        self.mode_select.place_forget()
        self.overview.place_forget()
        self.recreate.place_forget()
        self.train_pos.place_forget()
        # self.camera.place_forget()
        self.events.place_forget()
        self.auto_mode.place_forget()
        self.legends.place_forget()
        self.brightness.place_forget()
        self.backlight.place_forget()

        self.camera.place(x=18.0, y=204.0, width=1883.0, height=860.0)

    def button7pressed(self):
        print("button7 pressed")
        self.login_frame.place_forget()
        self.mode_select.place_forget()
        self.overview.place_forget()
        self.recreate.place_forget()
        self.train_pos.place_forget()
        self.camera.place_forget()
        # self.events.place_forget()
        self.auto_mode.place_forget()
        self.legends.place_forget()
        self.brightness.place_forget()
        self.backlight.place_forget()

        self.events.place(x=18.0, y=204.0, width=1883.0, height=860.0)

    def button8pressed(self):
        print("button8 pressed")
        self.login_frame.place_forget()
        self.mode_select.place_forget()
        self.overview.place_forget()
        self.recreate.place_forget()
        self.train_pos.place_forget()
        self.camera.place_forget()
        self.events.place_forget()
        # self.auto_mode.place_forget()
        self.legends.place_forget()
        self.brightness.place_forget()
        self.backlight.place_forget()

        self.auto_mode.place(x=18.0, y=204.0, width=1883.0, height=860.0)

    def button9pressed(self):
        print("button9 pressed")
        self.login_frame.place_forget()
        self.mode_select.place_forget()
        self.overview.place_forget()
        self.recreate.place_forget()
        self.train_pos.place_forget()
        self.camera.place_forget()
        self.events.place_forget()
        self.auto_mode.place_forget()
        # self.legends.place_forget()
        self.brightness.place_forget()
        self.backlight.place_forget()

        self.legends.place(x=18.0, y=204.0, width=1883.0, height=860.0)

    def button10pressed(self):
        print("button10 pressed")
        self.login_frame.place_forget()
        self.mode_select.place_forget()
        self.overview.place_forget()
        self.recreate.place_forget()
        self.train_pos.place_forget()
        self.camera.place_forget()
        self.events.place_forget()
        self.auto_mode.place_forget()
        self.legends.place_forget()
        # self.brightness.place_forget()
        self.backlight.place_forget()

        self.brightness.place(x=18.0, y=204.0, width=1883.0, height=860.0)
    
    def button11pressed(self):
        print("button11 pressed")
        self.login_frame.place_forget()
        self.mode_select.place_forget()
        self.overview.place_forget()
        self.recreate.place_forget()
        self.train_pos.place_forget()
        self.camera.place_forget()
        self.events.place_forget()
        self.auto_mode.place_forget()
        self.legends.place_forget()
        self.brightness.place_forget()
        # self.backlight.place_forget()

        self.backlight.place(x=18.0, y=204.0, width=1883.0, height=860.0)

# Timepass frame
class funFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #tkinter add a label
        self.label = Label(self, text="C0ngratulati0ns, you've succesfully failed life", font="-family {Roboto} -size -30 -weight normal -underline 0 -overstrike 0", fg="#ffffff", bg="#000000")
        self.label.place(x=4, y=3, width=1874, height=852)

# Timepass frame
class modeFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #tkinter add a label
        self.label = Label(self, text="Mode select window", font="-family {Roboto} -size -70 -weight normal -underline 0 -overstrike 0", fg="#ffffff", bg="#000000")
        self.label.place(x=4, y=3, width=1874, height=852)

# Timepass frame
class overviewFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #tkinter add a label
        self.label = Label(self, text="Train overview window", font="-family {Roboto} -size -70 -weight normal -underline 0 -overstrike 0", fg="#ffffff", bg="#000000")
        self.label.place(x=4, y=3, width=1874, height=852)

# Timepass frame
class recreateFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #tkinter add a label
        self.label = Label(self, text="Recreate scenario selection window", font="-family {Roboto} -size -70 -weight normal -underline 0 -overstrike 0", fg="#ffffff", bg="#000000")
        self.label.place(x=4, y=3, width=1874, height=852)

# Timepass frame
class trainposFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #tkinter add a label
        self.label = Label(self, text="Train position window", font="-family {Roboto} -size -70 -weight normal -underline 0 -overstrike 0", fg="#ffffff", bg="#000000")
        self.label.place(x=4, y=3, width=1874, height=852)

# Timepass frame
class cameraFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #tkinter add a label
        self.label = Label(self, text="Camera feed view window", font="-family {Roboto} -size -70 -weight normal -underline 0 -overstrike 0", fg="#ffffff", bg="#000000")
        self.label.place(x=4, y=3, width=1874, height=852)

# Timepass frame
class eventsFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #tkinter add a label
        self.label = Label(self, text="Events window", font="-family {Roboto} -size -70 -weight normal -underline 0 -overstrike 0", fg="#ffffff", bg="#000000")
        self.label.place(x=4, y=3, width=1874, height=852)

# Timepass frame
class autoFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #tkinter add a label
        self.label = Label(self, text="Automatic mode window", font="-family {Roboto} -size -70 -weight normal -underline 0 -overstrike 0", fg="#ffffff", bg="#000000")
        self.label.place(x=4, y=3, width=1874, height=852)

# Timepass frame
class legendFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #tkinter add a label
        self.label = Label(self, text="Legends view window", font="-family {Roboto} -size -70 -weight normal -underline 0 -overstrike 0", fg="#ffffff", bg="#000000")
        self.label.place(x=4, y=3, width=1874, height=852)

# Timepass frame
class backlightFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #tkinter add a label
        self.label = Label(self, text="Backlight control window", font="-family {Roboto} -size -70 -weight normal -underline 0 -overstrike 0", fg="#ffffff", bg="#000000")
        self.label.place(x=4, y=3, width=1874, height=852)

# Timepass frame
class brightnessFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #tkinter add a label
        self.label = Label(self, text="Brightness control window", font="-family {Roboto} -size -70 -weight normal -underline 0 -overstrike 0", fg="#ffffff", bg="#000000")
        self.label.place(x=4, y=3, width=1874, height=852)

# Run the program
if __name__ == "__main__":
    app = MainWindow(None)
    app.mainloop()

