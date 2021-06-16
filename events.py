from tkinter import *

root = Tk()
root.title("Events in Tkinter")
root.geometry("644x334")

# event.x gives x-position of mouse clicked
# event.y gives y-position of mouse clicked
def clickme(event):
    print(f"Button clicked at {event.x}, {event.y}")


widget = Button(root, text="Click me please")
widget.pack()

widget.bind('<Button-1>', clickme)

# it will quit the window on double click
widget.bind('<Double-1>', quit)

root.mainloop()