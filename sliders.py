from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Sliders in Tkinter")

# myslider = Scale(root, from_=0, to=100)
# myslider.pack()


def getdollar():
    tmsg.showinfo("Amount Credited",
                  f"We have credited {myslider2.get()} dollars to your bank")


Label(root, text="How mmany dollars do you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=25)
myslider2.set(50)
myslider2.pack()
Button(root, text="Get dollars", pady=10, command=getdollar).pack()

root.mainloop()
