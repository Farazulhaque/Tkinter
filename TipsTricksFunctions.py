from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("Tips, Tricks and Functions")
root.wm_iconbitmap("notepad.ico")
root.configure(background="grey")


width = root.winfo_screenmmwidth()
height = root.winfo_screenmmwidth()

print(f"{width}x{height}")
Button(text="Close", command=root.destroy).pack()


root.mainloop()
