from tkinter import * # Import tkinter module
from time import * # Import time module

def update():
    time = strftime("%I:%M:%S %p") # 12-hour clock
    time_label.config(text=time) # Update the label with the current time
    day = strftime("%A") # Day of the week
    day_label.config(text=day) # Update the label with the current day
    date = strftime("%B %d, %Y") # Month, day, year
    date_label.config(text=date) # Update the label with the current date
    window.after(1000,update) # Call the update function after 1 second
    

window = Tk() # Create a window





time_label = Label(window,font=("Arial",50),fg="white",bg="grey") # Create a label
time_label.pack() # Place the label in the window

day_label = Label(window,font=("Arial",30)) # Create a label
day_label.pack() # Place the label in the window

date_label = Label(window,font=("Arial",25)) # Create a label
date_label.pack() # Place the label in the window


update() # Call the update function






window.mainloop()