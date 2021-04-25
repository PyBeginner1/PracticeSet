from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry('500x700')
root.title("Treeview")

#create Style
style=ttk.Style()
#use theme
style.theme_use("clam")         #also can use 'default' or 'alt'
#configure treeview colours
style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=25, fieldbackground='silver')
style.map('Treeview', background=[('selected', 'blue')])


#creating treeview frame
tree_frame=Frame(root)
tree_frame.pack(pady=20)


#scrollbar for treeview
tree_scroll=Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)



#create Treeview
my_tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode='extended') #selectmode is 'extended' by default. There are 3 select modes->extended, none, browse
#extended-sel multiple items
#none- select no item
#browse - select single item
my_tree.pack()


#configure the scroll bar
tree_scroll.config(command=my_tree.yview)

#define columns
my_tree['columns']=('Name', 'Age', 'Favourite Pizza')


#format the columns
my_tree.column("#0", width=0, stretch=NO)        #treeview creates a invisible/ghost column so using it to make a column or use stretch =NO to make it invisible
my_tree.column('Name', width=120, anchor=W)
my_tree.column('Age', width=80, anchor=CENTER)
my_tree.column('Favourite Pizza', width=150, anchor=W)

#create headings of columns
my_tree.heading("#0", text='')
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Age", text="Age", anchor=CENTER)
my_tree.heading("Favourite Pizza", text="Food", anchor=W)

#add data-->Parent Data
'''
my_tree.insert(parent='', index='end', iid=0,text='Parent', values=('SN',23, 'Noodles'))
my_tree.insert(parent='', index='end', iid=1,text='Parent', values=('SR',23, 'Pizza'))
my_tree.insert(parent='', index='end', iid=2,text='Parent', values=('SS',16, 'Bir'))
my_tree.insert(parent='', index='end', iid=3,text='Parent', values=('SG',15, 'Dosa'))
my_tree.insert(parent='', index='end', iid=4,text='Parent', values=('SK',21, 'Idli'))
my_tree.insert(parent='', index='end', iid=5,text='Parent', values=('SM',29, 'Uppam'))
'''



#child
#my_tree.insert(parent='0', index='end', iid=6,text='Child', values=('NS',4, 'Cookies'))
#my_tree.insert(parent='1', index='end', iid=7,text='Child', values=('ST',3, 'Dark'))
#my_tree.insert(parent='2', index='end', iid=8,text='Child', values=('XK',7, 'Choc'))
#my_tree.insert(parent='3', index='end', iid=9,text='Child', values=('GG',2, 'Sprinkles'))
#my_tree.insert(parent='4', index='end', iid=10,text='Child', values=('WP',1, 'Oreo'))
#my_tree.insert(parent='5', index='end', iid=11,text='Child', values=('AS',4, 'Ice'))


#another way to add data from db
data=[
    ['SN',23, 'Noodles'],
    ['SR',23, 'Pizza'],
    ['SS',16, 'Bir'],
    ['SG',15, 'Dosa'],
    ['SK',21, 'Idli'],
    ['SM',29, 'Uppam'],['SN',23, 'Noodles'],
    ['SR',23, 'Pizza'],
    ['SS',16, 'Bir'],
    ['SG',15, 'Dosa'],
    ['SK',21, 'Idli'],
    ['SM',29, 'Uppam'],
    ['SN',23, 'Noodles'],
    ['SR',23, 'Pizza'],
    ['SS',16, 'Bir'],
    ['SG',15, 'Dosa'],
    ['SK',21, 'Idli'],
    ['SM',29, 'Uppam']

]

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="orange")

global count
count=0
for x in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(x[0],x[1],x[2]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(x[0], x[1], x[2]), tags=('oddrow',))

    count += 1




#create frame
add_frame=Frame(root)
add_frame.pack(pady=20)

#create labels
name=Label(add_frame, text='Name')
name.grid(row=0, column=0)

age=Label(add_frame, text="Age")
age.grid(row=0, column=1)

food=Label(add_frame, text="Favourite")
food.grid(row=0, column=2)



#create entry for labels
name_entry=Entry(add_frame)
name_entry.grid(row=1,column=0)

age_entry=Entry(add_frame)
age_entry.grid(row=1,column=1,padx=10)

food_entry=Entry(add_frame)
food_entry.grid(row=1,column=2,padx=10)



#adding record

def add_record():
    global count
    my_tree.insert(parent='', index='end',iid=count,text='', values=(name_entry.get(),age_entry.get(),food_entry.get()))
    count+=1

    name_entry.delete(0,END)
    age_entry.delete(0,END)
    food_entry.delete(0,END)


#remove all fnality
def remove_all():
    for x in my_tree.get_children():
        my_tree.delete(x)


#remove single record
def remove_record():
    x=my_tree.focus()       #focus on clicked item
    my_tree.delete(x)


#remove many fmality
def remove_many():
    my_tree.selection()   #selection is every clicked item
    for x in my_tree.selection():
        my_tree.delete(x)



#select record
def select_record():
    #empty the entry field
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    food_entry.delete(0, END)

    #grab the record
    selected = my_tree.focus()              #selected has the list number
    #temp_label.config(text=selected)

    #grab the values
    values =my_tree.item(selected, 'values')

    #put the selected record into entry field
    name_entry.insert(0,values[0])
    age_entry.insert(0,values[1])
    food_entry.insert(0,values[2])

#update selected record
def update_button():
    #grab the record
    selected=my_tree.focus()
    #update the record
    my_tree.item(selected, text='', values=(name_entry.get(), age_entry.get(), food_entry.get()))

    #empty the enry fields
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    food_entry.delete(0, END)

#create clicker for binding
def clicker(e):
    select_record()

#move up
def move_up():
    rows=my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

def move_down():
    rows=my_tree.selection()
    for row in reversed(rows):              #reversed(rows) imp for moving down
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)



#create add record button
add_record=Button(root, text="Add record", command=add_record)
add_record.pack()

#remove all button
remove_all=Button(root, text='Remove All', command=remove_all)
remove_all.pack(pady=10)

remove_record=Button(root, text="Remove Record", command=remove_record)
remove_record.pack(pady=10)

remove_many=Button(root, text="Remove Many", command=remove_many)
remove_many.pack(pady=10)

select_button=Button(root, text="Select Record", command=select_record)
select_button.pack(pady=10)

update_button=Button(root, text="Update Record ", command=update_button)
update_button.pack(pady=10)

move_up=Button(root, text="Move Up", command=move_up)
move_up.pack(pady=10)

move_down=Button(root, text="Move Down", command=move_down)
move_down.pack(pady=10)

temp_label=Label(root)
temp_label.pack(pady=10)

#create a binding so that we can select a record by double click
my_tree.bind("<Double-1>", clicker)

#bininding using button release
#my_tree.bind("<ButtonRelease-1>", clicker)

root.mainloop()
