from tkinter import *

root = Tk()
root.geometry("500x600")
root.title("Calculator in Tkinter")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


root.mainloop()
