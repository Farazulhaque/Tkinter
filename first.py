from tkinter import *

root = Tk()

# gui logic here

# width x Height
root.geometry("600x400")

# width, height
root.minsize(300, 100)

# width, height
root.maxsize(1200, 1000)

label = Label(text="My First GUI")
label.pack()

root.mainloop()
