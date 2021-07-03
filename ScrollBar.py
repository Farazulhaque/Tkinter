from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("Scroll Bar")

# For connecting scroll bar to a widget
# 1. widget (yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command = widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# fOR LIST BOX
# listbox = Listbox(root, yscrollcommand=scrollbar.set)
# for i in range(344):
#     listbox.insert(END, f"Item {i}")

# For simple notepad
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)

# listbox.pack(fill="both", padx=22)
scrollbar.config(command=text.yview)
root.mainloop()
