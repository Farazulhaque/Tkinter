from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
# root.geometry("455x233")
root.title("Radio Buttons in Tkinter")


def order():
    total_cost = 10
    if size.get() == "medium":
        total_cost += 1.50
    elif size.get() == "large":
        total_cost += 3.00
    if toppings.get() == "pepperoni":
        total_cost += 0.5
    elif toppings.get() == "olives":
        total_cost += 1.00
    elif toppings.get() == "mushroom":
        total_cost += 1.5

    tmsg.showinfo("Order Received",
                  f"Thank You {namevalue.get()}. \
                      We have received your order.\n\
                          Total Prce = Rs.{total_cost} \nThanks for ordering")


name = Label(root, text="Name")
name.grid(row=1, column=2)
namevalue = StringVar()
nameentry = Entry(root, textvariable=namevalue)
nameentry.grid(row=1, column=3)

crust = StringVar()
crust.set("regular")
Label(root, text="Pick one of the three crust",
      padx=14).grid(row=2, column=1, columnspan=2)
radio = Radiobutton(root, text="Thin",
                    variable=crust, value="thin").grid(row=3, column=1)
radio = Radiobutton(root, text="Regular",
                    variable=crust, value="regular").grid(row=3, column=2)
radio = Radiobutton(root, text="Deep Dish",
                    variable=crust, value="deepdish").grid(row=3, column=3)


sauces = StringVar()
sauces.set("regular")
Label(root, text="Pick one of the three sauces", justify=LEFT,
      padx=14).grid(row=4, column=1, columnspan=2)
radio = Radiobutton(root, text="BBQ",
                    variable=sauces, value="bbq").grid(row=5, column=1)
radio = Radiobutton(root, text="Regular",
                    variable=sauces, value="regular").grid(row=5, column=2)
radio = Radiobutton(root, text="Alfredo",
                    variable=sauces, value="alfredo").grid(row=5, column=3)


toppings = StringVar()
toppings.set("olives")
Label(root, text="Pick one of the three toppings", justify=LEFT,
      padx=14).grid(row=6, column=1, columnspan=2)
radio = Radiobutton(root, text="Pepperoni",
                    variable=toppings, value="pepperoni").grid(row=7, column=1)
radio = Radiobutton(root, text="Olives",
                    variable=toppings, value="olives").grid(row=7, column=2)
radio = Radiobutton(root, text="Mushroom",
                    variable=toppings, value="mushroom").grid(row=7, column=3)

size = StringVar()
size.set("medium")
Label(root, text="Pick one of the three size", justify=LEFT,
      padx=14).grid(row=8, column=1, columnspan=2)
radio = Radiobutton(root, text="Small",
                    variable=size, value="small").grid(row=9, column=1)
radio = Radiobutton(root, text="Medium",
                    variable=size, value="medium").grid(row=9, column=2)
radio = Radiobutton(root, text="Large",
                    variable=size, value="large").grid(row=9, column=3)


Button(text="Order Now", command=order).grid(row=11, column=2)


root.mainloop()
