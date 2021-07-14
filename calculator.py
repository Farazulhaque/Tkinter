from tkinter import *

root = Tk()
root.geometry("295x415")
root.wm_iconbitmap("calculator.ico")
root.title("Calculator in Tkinter")


def click(event):
    global scvalue
    text = event.widget.cget("text")
    # if text == "Q":
    #     event.widget.quit
    if text == "=":
        scvalue.set(eval(scvalue.get()))
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + str(text))
        screen.update()


scvalue = StringVar()
scvalue.set("")
screen = Entry(root, bg="grey", fg="white",
               textvar=scvalue, font="lucida 25 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

nums = ["Q", "C", "<", "/", 7, 8, 9, "*", 4,
        5, 6, "-", 1, 2, 3, "+", "00", 0, ".", "="]
frame = Frame(root, bg="#898f8b")
for i in range(1, len(nums)+1):
    btn = Button(frame, text=nums[i-1], font="lucida 25 ",
                 bg="grey", fg="white", width=3, height=1, relief=FLAT)
    btn.pack(side=LEFT, padx=1, pady=1)
    btn.bind("<Button-1>", click)
    if i % 4 == 0:
        frame.pack()
        frame = Frame(root, bg="#898f8b")


root.mainloop()
