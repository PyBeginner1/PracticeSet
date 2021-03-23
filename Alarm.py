import time
from tkinter import *
from tkinter import messagebox

# creating Tk window
root = Tk()

root.geometry("300x250")
root.title("Alarm")

# Declaration of variables
hour = StringVar()
minute = StringVar()
second = StringVar()

#setting to default 0
hour.set("00")
minute.set("00")
second.set("00")

#creating entry class to take input from user
hourEntry = Entry(root, width=3, font=('Arial', 18 , ""), textvariable=hour)
hourEntry.place(x=80, y=20)
minuteEntry = Entry(root, width=3, font=('Arial', 18 , ""), textvariable=minute)
minuteEntry.place(x=130, y=20)
secondEntry = Entry(root, width=3, font=('Arial', 18 , ""), textvariable=second)
secondEntry.place(x=180, y=20)

def submit():
    try:
        # the input provided by the user is stored in temp
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Invalid")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        #using format () method to store the value up to # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("Time Countdown, Times Up")
        temp -= 1

#button widget
btn = Button(root, text = "Set Countdown", bd='5', command = submit)
btn.place(x=70, y=120)

root.mainloop()



