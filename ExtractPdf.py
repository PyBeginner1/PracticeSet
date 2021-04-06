from tkinter import *
import PyPDF2
from PIL import Image,ImageTk
from tkinter import filedialog
from functions import extract_images

#global variable
page_contents = []  #copytext
all_images = []     #saveAll
img_idx = [0]       #save

root =Tk()

#logo & browse button
header = Frame(root, height = 175, width =800, bg = 'white')
header.grid(columnspan = 3, rowspan =2, row=0)

#creating text widget in row 2
img_menu = Frame(root, height = 175, width =800)
img_menu.grid(columnspan = 3, rowspan =2, row=2)
#creating text widget
what_img = Label(root, text="Image 1 of 5", font =("Shanti", 10))
what_img.grid(column=1, row=2)


#create a single row for mul options
save_img = Frame(root, height = 60, width =800, bg = '#c8c8c8')
save_img.grid(columnspan = 3, rowspan =1, row=3)

def copy_text(content):
    root.clipboard_clear()
    root.clipboard_append(content)

def save_al(images):
    counter = 1
    for i in images:
        if i.mode != 'RGB':
            i = i.convert('RGB')

        i.save("img" + str(counter) + ".png", format='png')
        counter += 1


def save_img(i):
    if i.mode != 'RGB':
        i =i.convert_('RGB')
    i.save("img.png",format='png')

#creating buttons for middle singular row
copyText_btn = Button(root, text="Copy Text",command=lambda:copy_text(page_contents), font=("Times New Roman", 10), height = 1, width =15)
saveAll_btn = Button(root, text="Save All Files",command=lambda:save_al[all_images], font=("Times New Roman", 10), height = 1, width =15)
save_btn = Button(root, text="Save",command=lambda:save_img(all_images[img_idx]) ,font=("Times New Roman", 10), height = 1, width =15)
#grid to display buttons
copyText_btn.grid(row=3, column =0)
saveAll_btn.grid(row=3, column =1)
save_btn.grid(row=3, column =2)


#display content
main_content = Frame(root, height=250, width = 800, bg='#C9913A')
main_content.grid(columnspan =3, rowspan =2, row =4)



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
        page_content = page_content.replace('\u2122', "'")
        #show textbox on row 4 col 0
        display_textbox(page_content, 4, 0, root)

        #to store mul files
        page_contents.append(page_content)

        #to extract image from the pdf file
        images = extract_images(page)
        #in order to select 1 image at a time
        img = images[img_idx[-1]]

        #we need to resize the image because now its too large
        def resize_image(img):
            width, height = int(img.size[0]), int(img.size[1])
            if width > height:
                height = int(300/width*height)
                width =300
            elif height > width:
                width = int(250/height*width)
                height =250
            else:
                width, height = 250,250
            img = img.resize((width, height))
            return img

        def display_images(img):
            img = resize_image(img)
            img = ImageTk.PhotoImage(img)
            img_label = Label(image=img, bg="white")
            # create image
            img_label.image = img
            img_label.grid(column=2, row=4, rowspan =2)
            return img_label

        display_images(img)



        #set button to Browse after loading...
        browse_var.set("Browse")

def display_textbox(content, ro, col, root):
    text_box = Text(root, height=10, width=30, padx=10, pady=10)
    text_box.insert(1.0, content)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=col, row=ro, sticky=SW, padx=25, pady=25)



def display_logo(url, row, column):
    img = Image.open(url)
    #resize image
    img = img.resize((int(img.size[0]/1.5),int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img, bg="white")
    #create image
    img_label.image = img
    img_label.grid(column=column, row=row, rowspan=2, sticky=NW, padx=20, pady=40)


display_logo('logo.png',  0,  0)


#creating functionality(next or previous image) for button(left & right arrow) for text widget in row 2
def display_icon(url, row, column,stick):
    icon = Image.open(url)
    icon=icon.resize((20,20))
    icon = ImageTk.PhotoImage(icon)
    icon_btn = Button(image = icon, height=25, width=25)
    icon_btn.image= icon
    #sticky command is used to bring the buttons much more closer & to call it you have to Specify N,S,E,W
    icon_btn.grid(row=row, column=column, sticky=stick)
display_icon("arrow_l.png",2 ,0, E )
display_icon("arrow_r.png",2, 2, W)



#instructions
instructions = Label(root, text = "Select PDF File:", font = 'Raleway')
instructions.grid(column = 2, row = 0)

#create a variable to store the text
browse_var = StringVar()
browse_btn = Button(root, textvariable = browse_var,command = openFile, font = "raleway", bg = "#55ABB3")
#set is used to name the button
browse_var.set("Browse")
browse_btn.grid(column = 2, row = 1)

root.mainloop()




