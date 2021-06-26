from tkinter import *

root = Tk()
root.geometry("733x566")
root.title("Menus and Submenus")


def myfunc():
    print("Success")


# use these to create non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="file", command=mymenu)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)
mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New File", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.configure(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Cut", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.configure(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

root.mainloop()
