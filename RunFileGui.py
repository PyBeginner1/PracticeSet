import tkinter as tk
#filedialog helps us pick files
from tkinter import filedialog
#os helps in interacting with the system
import os

apps = []

root = tk.Tk()
root.geometry("700x700")
#code for some cool colour
root.config(bg='#263D42')

#to not lose the file that was opened previously after quiting
if os.path.isfile('save.txt'):
    with open ('save.txt','r') as f:
        tempApps=f.read()
        tempApps=tempApps.split(',')
        apps=[x for x in tempApps if x.strip()]

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#to open a file
def addApp():
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app,fg ='grey')
        label.pack()

#run a file
def openApp():
    for app in apps:
        os.startfile(app)

openFile = tk.Button(root, text="Open File", bg="#263D42", fg="white", command=addApp).pack()
runApps = tk.Button(root, text="Run Apps", bg="#263D42", fg='white',command=openApp).pack()

for app in apps:
    label=tk.Label(frame, text = app)
    label.pack()



root.mainloop()

#saving file so that it doesnt go away after quitting
with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')