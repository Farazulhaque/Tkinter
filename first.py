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

# ======================================================
# Grid Layout
def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")

user = Label(root, text = "Username")
password = Label(root, text = "Password")
user.grid()
password.grid(row=1)

# Variable classes in Tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row = 0, column = 1)
passentry.grid(row = 1, column = 1)

Button(text="Submit", command=getvals).grid()

# ======================================================
# BUTTONS

# def hello():
#     print("Hello")


# frame = Frame(root, borderwidth=6, bg="grey", relief=RIDGE)
# frame.pack(side=LEFT, anchor="nw")

# b1 = Button(frame, fg="red", text="Click me", command=hello)
# b1.pack(side="left", padx=23)

# b2 = Button(frame, fg="red", text="Click me")
# b2.pack(side="left", padx=23)

# b3 = Button(frame, fg="red", text="Click me")
# b3.pack(side="left", padx=23)

# b4 = Button(frame, fg="red", text="Click me")
# b4.pack(side="left", padx=23)

# # ======================================================
# # FRAMES
# f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
# f1.pack(side=LEFT, fill="y")

# f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
# f2.pack(side=TOP, fill="x")

# l = Label(f1, text="Project Tkinter - Notepad")
# l.pack(pady=42)

# l = Label(f2, text="Project Tkinter - Notepad",
#           font="Helvetica 16 bold", fg="red", pady=5)
# l.pack(pady=42)

# ======================================================
# Important Label Options
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
