import tkinter


class My_GUI:
    def __init__(self):
        self.main_form = tkinter.Tk()
        self.main_form.title("Greeting")
        # self.main_form.geometry("425x125")

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.lblName = tkinter.Label(
            self.top_frame, text="Celsius", font=("", 20, "bold"))

        self.lblSmiley = tkinter.Label(
            self.top_frame, text="\N{DEGREE CELSIUS}", font=("", 20, "bold"))

        self.lblOutput = tkinter.Label(
            self.bottom_frame, font=("", 20, "bold"))

        self.entName = tkinter.Entry(self.top_frame, font=(
            "", 20, "bold"), width=10, relief="solid", borderwidth=2, justify="right")

        self.btnGreet = tkinter.Button(self.top_frame, font=(
            "", 20, "bold"), text="\N{RIGHTWARDS BLACK ARROW}\N{DEGREE FAHRENHEIT}",
            command=self.greeting, relief="raised", borderwidth=5, bg="blue", fg="white")

        self.top_frame.pack()
        self.bottom_frame.pack()

        self.lblName.pack(side="left", pady=10)
        self.entName.pack(side="left")
        self.lblSmiley.pack(side="left")
        self.btnGreet.pack(side="left", padx=10, pady=10, ipadx=25, ipady=10)

        self.lblOutput.pack()

        self.entName.focus()

        tkinter.mainloop()

    def greeting(self):
        c = self.entName.get()
        f = (float(c) * 9/5) + 32
        self.lblOutput["text"] = f"{f}\u00B0F"
        self.entName.delete(0, 'end')


my_gui = My_GUI()
