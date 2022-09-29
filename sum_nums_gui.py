from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Read a file and calculate sum")
root.geometry("400x200")

def clickme(event):
	sum = 0
	with open('numbers.txt') as f:
		for num in f:
			num = num.strip()
			sum += int(num)
	print(sum)
	tmsg.showinfo("Total", "Total sum of numbers= " + str(sum))


widget = Button(root, text="Read file and calculate sum")
widget.pack()

widget.bind('<Button-1>', clickme)

root.mainloop()


