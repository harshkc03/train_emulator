# function to create clock gui using tkinter
def clock():
    import tkinter as tk
    import time
    # create window
    window = tk.Tk()
    # set window size
    window.geometry("500x500")
    # set window title
    window.title("Clock")
    # set window background color
    window.configure(background="black")
    # create label
    label = tk.Label(window, text="", font=("times", 100, "bold"), bg="black", fg="white")
    # set label position
    label.place(x=0, y=0, relwidth=1, relheight=1)
    # create function to update time
    def tick():
        # get time
        time1 = time.strftime("%H:%M:%S")
        # set label text to time
        label.config(text=time1)
        # call tick function after 1 second
        window.after(1000, tick)
    # call tick function
    tick()
    # start window
    window.mainloop()

clock()