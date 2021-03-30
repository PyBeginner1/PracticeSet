from tkinter import *
import calendar


def showCal():
    new_gui = Tk()                                                                         # Create a GUI window
    new_gui.config(background="white")
    new_gui.title("Calendar")
    new_gui.geometry("550x600")
    fetch_year = int(year_field.get())                                                      # Create a GUI window
    cal_content = calendar.calendar(fetch_year)                                             # calendar method of calendar module return the calendar of the given year .
    cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")                # Create a label for showing the content of the calender
    cal_year.grid(row=5, column=1, padx=20)                                                 # grid method is used for placing the widgets at respective positions in table like structure
    new_gui.mainloop()                                                                      # start the GUI

if __name__ == '__main__':
    gui = Tk()
    gui.config(background="white")
    gui.title("Calendar")
    gui.geometry("250x140")
    cal = Label(gui, text = "Calendar", bg="dark gray",                                     # Create a CALENDAR : label with specified font and size
                font=("times", 28, 'bold'))                                                 # Create a Enter Year : label
    year=Label(gui, text = "Enter Year", bg="light green")                                  # Create a text entry box for filling or typing the information
    year_field = Entry(gui)
    submit = Button(gui, text = "Submit", fg="Black",  bg="Red", command = showCal)
    exit = Button(gui, text = "Exit",fg="Black", bg="Red", command = exit)
    cal.grid(row = 1, column =1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    submit.grid(row=4, column=1)
    exit.grid(row=6, column=1)
    gui.mainloop()