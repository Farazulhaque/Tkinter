from tkinter import *
from tkinter import font
import tkinter.messagebox as tmsg

root = Tk()
# root.geometry("455x233")
root.title("Radio Buttons in Tkinter")


def order():

    tmsg.showinfo("Order Received", f"Thank You. We have received your order for {size.get()} size .\n\
                          \nThanks for ordering")


Label(root, text="Sam's Coffee Shop", font=(
    "", 16, "bold")).grid(row=1, column=2)

size = StringVar()
size.set("medium")
Label(root, text="Pick one of the three size", justify=LEFT,
      padx=14).grid(row=3, column=1)
radio = Radiobutton(root, text="Small",
                    variable=size, value="small").grid(row=4, column=1)
radio = Radiobutton(root, text="Medium",
                    variable=size, value="medium").grid(row=4, column=2)
radio = Radiobutton(root, text="Large",
                    variable=size, value="large").grid(row=4, column=3)

ingred = StringVar()
ingred.set("black")
Label(root, text="Pick one of the three ingredients",
      padx=14).grid(row=5, column=1)
radio = Radiobutton(root, text="Black",
                    variable=ingred, value="black").grid(row=6, column=1)
radio = Radiobutton(root, text="Sugar",
                    variable=ingred, value="sugar").grid(row=6, column=2)
radio = Radiobutton(root, text="Creamer",
                    variable=ingred, value="creamer").grid(row=6, column=3)

Button(text="Order Now", command=order).grid(row=8, column=2)


root.mainloop()
