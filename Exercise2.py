# Create a GUI window which takes as input width and height
# and upon clicking apply , it should be able to change its size accordingly

from tkinter import *

root = Tk()
root.geometry("344x233")
root.title("Exercise 2")

def update():
    print("Updating the GUI")
    root.geometry(f"{width.get()}x{height.get()}")

width = StringVar()
height = StringVar()
Entry(root, textvariable=width).pack()
Entry(root, textvariable=height).pack()
Button(root, text="Apply", command=update).pack()

root.mainloop()