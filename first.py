from tkinter import *
from PIL import Image, ImageTk
root = Tk()

# gui logic here

# width x Height
root.geometry("600x400")

# Set title
root.title("My GUI Using Tkinter")

# width, height
root.minsize(300, 100)

# width, height
root.maxsize(1200, 1000)

f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Project Tkinter - Notepad")
l.pack(pady=42)

l = Label(f2, text="Project Tkinter - Notepad",
          font="Helvetica 16 bold", fg="red", pady=5)
l.pack(pady=42)
# # Important Label Options
# bg = background
# fg = foreground
# font = sets the font
# padx = x padding
# pady = y padding
# font = ("comicsansms", 19, "italic")
# font = "comicsansms 19 italic"
# relief = border styling = SUNKEN, RAISED, GROOVE, RIDGE

# title_label = Label(text="Hello!! \n How are you?", bg="red", fg="white",
#                     padx=20, pady=20, font="comicsansms 19 italic", borderwidth=3, relief=RIDGE)
# # title_label.pack(anchor = "nw")
# title_label.pack(side = "left", fill= Y)


# Important Pack options
# anchor = nw, ne
# side = top, bottom, left, right
# fill = x, y


# label = Label(text="My First GUI",)
# label.pack()

# # Add image
# photo = PhotoImage(file="1.png")
# label = Label(image=photo)
# label.pack()

# # for JPG image
# image = Image.open("2.jpg")
# photo = ImageTk.PhotoImage(image)
# label = Label(image=photo)
# label.pack()

root.mainloop()
