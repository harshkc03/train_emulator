# fucntion to create clock using Tkinter

# import Tkinter
import tkinter as tk
import datetime
# create a window
window = tk.Tk()
# set the window size
window.geometry("600x200")
# set the window title
window.title("Clock")
# create a label
label = tk.Label(window, text="", font=("Arial", 100))
# set the label position
label.place(x=0, y=0, width=600, height=200)
# create a function to update the clock
def update_clock():
    # get the current time
    time = datetime.datetime.now()
    # get the hour, minute and second
    h = time.hour
    m = time.minute
    s = time.second
    # convert to 12 hour format
    if h > 12:
        h -= 12
    # add a 0 before the hour, minute and second if less than 10
    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    if s < 10:
        s = "0" + str(s)
    print(str(h) + ":" + str(m) + ":" + str(s))
    # update the label
    label.config(text=str(h) + ":" + str(m) + ":" + str(s))
    # call the update_clock function after 1 second
    window.after(1000, update_clock)
# call the update_clock function
update_clock()
# start the mainloop
window.mainloop()

