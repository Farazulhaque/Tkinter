from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Radio Buttons")


def order():
    tmsg.showinfo("Order Received",
                  f"We have received your order for {var.get()}. Thanks for ordering")


# var = IntVar()
var = StringVar()
var.set("Biryani")
Label(root, text="What would you like to have sir?",
      font="lucida 19 bold", justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text="Biryani", padx=14,
                    variable=var, value="Biryani").pack(anchor="w")
radio = Radiobutton(root, text="Idli", padx=14,
                    variable=var, value="Idli").pack(anchor="w")
radio = Radiobutton(root, text="Paratha", padx=14,
                    variable=var, value="Paratha").pack(anchor="w")
radio = Radiobutton(root, text="Samosa", padx=14,
                    variable=var, value="Samosa").pack(anchor="w")

Button(text="Order Now", command=order).pack()


root.mainloop()
