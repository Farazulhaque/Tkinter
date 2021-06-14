from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("My GUI")


can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# The line goes from point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="green")

# To create a rectangle specify the parameters in this order -
# coors of top-left and coors of bottom-right
can_widget.create_rectangle(100, 50, 700, 350, fill="cyan")

# create circle shape inside a rectangle co-ordinates
can_widget.create_oval(110, 60, 690, 340, fill="white")

# Write text
can_widget.create_text(400, 200, text="Python Canvas")


root.mainloop()
