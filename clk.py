from tkinter import *
from time import *

def update():

    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    
    dam_string = strftime("%j")
    dam_label.config(text="Day of the year " +dam_string)
    
    window.after(1000,update)


window = Tk()

time_label = Label(window,font=("Arial",50),fg="red",bg="black")
time_label.pack()

day_label = Label(window,font=("italic",25,"bold"),fg="green")
day_label.pack()

date_label = Label(window,font=("italic",30),fg="blue")
date_label.pack()

dam_label = Label(window,font=("italic",25,"bold"),fg="orange")
dam_label.pack()

update()
window.mainloop()