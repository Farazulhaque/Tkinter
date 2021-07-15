from tkinter import *

root = Tk()
root.geometry("295x415")
root.wm_iconbitmap("calculator.ico")
root.title("Calculator in Tkinter")


def buttonclick(event):
    value = str(event.widget.cget("text"))
    # print(value)

    if value == "=":
        try:
            if scvalue.get().isdigit():
                finalvalue = int(scvalue.get())
            else:
                # eval() is in-built function to perform maths operations
                finalvalue = eval(scvalue.get())
                if int(finalvalue) == float(finalvalue):
                    scvalue.set(finalvalue)
                # To round upto 3 digits
                else:
                    scvalue.set(round(finalvalue, 3))
                screen.update()
        except:
            scvalue.set(scvalue.get()[:-1])
            screen.update()

    elif value == "⌫":  # for backspace
        scvalue.set(scvalue.get()[:-1])
        screen.update()

    elif value == "C":  # for clearing the screen.
        scvalue.set("")
        screen.update()

    # adding text in screen
    else:
        scvalue.set(scvalue.get() + value)
        screen.update()


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, bg="#666262", fg="white",
               textvar=scvalue, font="lucida 25 bold", justify=RIGHT, borderwidth=2, relief=RIDGE)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

nums = ["Q", "C", "⌫", "/", 7, 8, 9, "*", 4,
        5, 6, "-", 1, 2, 3, "+", "00", 0, ".", "="]
frame = Frame(root, bg="#898f8b")
for i in range(1, len(nums)+1):
    btn = Button(frame, text=nums[i-1], font="lucida 25 ",
                 bg="grey", fg="white", width=3, height=1, relief=FLAT)
    btn.pack(side=LEFT, padx=1, pady=1)

    # here Q stands for quit -> closing calculator window
    # quit is in-built function n tkinter library to close the window
    if nums[i-1] == "Q":
        btn.bind("<Button-1>", quit)

    # else call buttonclick function on click
    else:
        btn.bind("<Button-1>", buttonclick)

    # Pack frame after every 4 buttons
    if i % 4 == 0:
        frame.pack()
        frame = Frame(root, bg="#898f8b")


root.mainloop()
