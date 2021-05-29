from tkinter import *
from PIL import Image, ImageTk
root = Tk()

# gui logic here

# width x Height
root.geometry("600x400")

# width, height
root.minsize(300, 100)

# width, height
root.maxsize(1200, 1000)

label = Label(text="My First GUI",)
label.pack()

# Add image
# photo = PhotoImage(file="1.png")
# label = Label(image=photo)
# label.pack()

# for JPG image
image = Image.open("2.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.pack()

root.mainloop()
