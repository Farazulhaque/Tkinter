from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("Status Bar in Tkinter")


def upload():
    statusvar.set("Uploading...")
    # To update the value of statusvar
    sbar.update()
    import time
    time.sleep(5)
    statusvar.set("Done.")


statusvar = StringVar()
statusvar.set("Ready")
# anchor="w" sets the direction of text
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
# side=BOTTOM packs the content sbar to bottom
# fill=X fils the sbar horizontally
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack()
root.mainloop()
