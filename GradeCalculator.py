import tkinter
from tkinter import *


root = Tk()
root.geometry("500x400")
root.title('Grade Calculator')

def marks_calculate():
    maths = int(maths_entry.get())
    science = int(science_entry.get())
    social = int(social_entry.get())

    total = maths + science+ social
    Label(root, text = total, font = 'Shanti 15').place(x = 200, y=170)

    average = (maths + science + social) / 3
    Label(root, text = average, font = 'Shanti 14').place(x = 200, y = 220)

    if average < 40:
        grade = 'Fail'
    elif average >= 40 and average <= 50:
        grade = "Pass"
    else:
        grade ='Distinction'
    Label(root, text = grade, font = 'Shanti 14').place(x = 200, y =270)



sub_1 = Label(root, text = 'Maths', font = 'Shanti  14')
sub_1.place( x= 50, y = 20)
sub_2 = Label(root, text = 'Science', font = 'Shanti  14')
sub_2.place( x= 50, y = 70)
sub_3 = Label(root, text = 'Social', font = 'Shanti  14')
sub_3.place( x= 50, y = 120)
total_marks = Label(root, text = 'Total Marks' , font = 'Shanti  14')
total_marks.place(x = 50, y = 170)
avg_marks = Label(root, text = 'Average Marks' , font = 'Shanti  14')
avg_marks.place(x = 50, y = 220)
grade_score = Label(root, text = 'Grades' , font = 'Shanti  14')
grade_score.place(x = 50, y = 270)

maths_marks = StringVar()
science_marks = StringVar()
social_marks = StringVar()

maths_entry = Entry(root, textvariable = maths_marks, width = 15)
maths_entry.place(x = 200, y = 25)

science_entry = Entry(root, textvariable =science_marks, width = 15)
science_entry.place(x = 200, y = 75)

social_entry = Entry(root, textvariable =social_marks, width = 15)
social_entry.place(x = 200, y = 120)


Button(root, text = 'Calculate', bd = 5, bg = 'grey', command = marks_calculate).place(x = 200, y =330)
Button(root, text = 'Exit', bd = 5, bg = 'grey', command = lambda: exit()).place(x = 350, y = 330)





root.mainloop()
