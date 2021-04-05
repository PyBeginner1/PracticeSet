import tkinter as tk
import PyPDF2
from PIL import Image,ImageTk
from tkinter import filedialog

root =tk.Tk()

canvas = tk.Canvas(root, width = 600, height = 300)
#columnspan & rowspan divides the window into equal parts horizontally & vertically
canvas.grid(columnspan = 3, rowspan = 3)

#logo
logo = Image.open("logo.png")
#convert pil image to tkinter image
logo =ImageTk.PhotoImage(logo)
#create label
logo_label=tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column = 1, row = 0)

def openFile():
    browse_var.set("loading...")
    filename = filedialog.askopenfile(parent = root,mode = 'rb', title ="Choose File", filetype = [("Pdf files", "*.pdf")])
    if filename:
        #open to read
        read_pdf = PyPDF2.PdfFileReader(filename)
        #go to page 1 of file
        page = read_pdf.getPage(0)
        #display the content on page 1
        page_content = page.extractText()

        #we wanna display the content on tkinter window so we create a new variable
        text_box = tk.Text(root, width=50, height=10, padx =15, pady=15)
        text_box.insert(1.0,page_content)
        text_box.tag_configure("center", justify = "center")
        text_box.tag_add("center",1.0, "end")
        text_box.grid(column=1, row =3)

        browse_var.set("Browse")

#instructions
instructions = tk.Label(root, text = "Select PDF File:", font = 'Raleway')
instructions.grid(column = 1, row = 1)

#create a variable to store the text
browse_var = tk.StringVar()
browse_btn = tk.Button(root, textvariable = browse_var,command = openFile, font = "raleway", bg = "#273d2f")
#set is used to name the button
browse_var.set("Browse")
browse_btn.grid(column = 1, row = 2)

canvas = tk.Canvas(root, width = 300, height = 250)
canvas.grid(columnspan = 3, rowspan = 3)




root.mainloop()