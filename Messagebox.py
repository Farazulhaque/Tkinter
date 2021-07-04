from tkinter import *
import tkinter.messagebox as tmsg


root = Tk()
root.geometry("733x566")
root.title("Message Box in Tkinter")


def myfunc():
    print("Success")


def help():
    print("I will help you.")
    a = tmsg.showinfo("Help", "I will help you with this gui")
    # print(a)


def rate():
    print("Rate Us")
    value = tmsg.askquestion("Was your experience good?",
                             "You used this GUI, Was your experience good? ")
    # print(value)
    if value == "yes":
        msg = "Great. Rate us on app store please"
    else:
        msg = "Tell us what went wrong"
    tmsg.showinfo("Experience", msg)


def arisha():
    ans = tmsg.askretrycancel("Arisha se dosti karlo",
                              "Sorry Arisha nhi dosti karegi")
    if ans:
        tmsg.showwarning("Warning", "Retry karne pe bhi nhi karegi")
    else:
        tmsg.showwarning("Warning", "Achcha hua retry nhi kiya")


mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New File", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.configure(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Cut", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.configure(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="Befriend Arisha", command=arisha)
root.configure(menu=mainmenu)
mainmenu.add_cascade(label="Help", menu=m3)

root.mainloop()
