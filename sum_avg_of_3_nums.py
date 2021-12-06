import tkinter


class GameAvg:
    def calc_avg(self):
        self.game1 = float(self.game1_entry.get())
        self.game2 = float(self.game2_entry.get())
        self.game3 = float(self.game3_entry.get())
        self.average = (self.game1 + self.game2 + self.game3)/3.0
        self.avg.set(self.average)

    def calc_sum(self):
        self.game1 = float(self.game1_entry.get())
        self.game2 = float(self.game2_entry.get())
        self.game3 = float(self.game3_entry.get())
        self.summed = self.game1 + self.game2 + self.game3
        self.sum.set(self.summed)

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.game1_frame = tkinter.Frame(self.main_window)
        self.game2_frame = tkinter.Frame(self.main_window)
        self.game3_frame = tkinter.Frame(self.main_window)
        self.average_frame = tkinter.Frame(self.main_window)
        self.sum_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.game1_label = tkinter.Label(
            self.game1_frame, text="Enter your points for game1: ")
        self.game1_entry = tkinter.Entry(self.game1_frame, width=10)
        self.game1_label.pack(side='left')
        self.game1_entry.pack(side='left')

        self.game2_label = tkinter.Label(
            self.game2_frame, text="Enter your points for game2: ")
        self.game2_entry = tkinter.Entry(self.game2_frame, width=10)
        self.game2_label.pack(side='left')
        self.game2_entry.pack(side='left')

        self.game3_label = tkinter.Label(
            self.game3_frame, text="Enter your points for game3: ")
        self.game3_entry = tkinter.Entry(self.game3_frame, width=10)
        self.game3_label.pack(side='left')
        self.game3_entry.pack(side='left')

        self.result_label = tkinter.Label(self.average_frame, text="Average: ")
        self.avg = tkinter.StringVar()
        self.average_label = tkinter.Label(
            self.average_frame, textvariable=self.avg)
        self.result_label.pack(side='left')
        self.average_label.pack(side='left')

        self.result_label = tkinter.Label(self.sum_frame, text='Sum: ')
        self.sum = tkinter.StringVar()
        self.sum_label = tkinter.Label(self.sum_frame, textvariable=self.sum)
        self.result_label.pack(side='left')
        self.sum_label.pack(side='left')

        self.avg_button = tkinter.Button(
            self.button_frame, text='Average', command=self.calc_avg)
        self.sum_button = tkinter.Button(
            self.button_frame, text='Sum', command=self.calc_sum)
        self.quit_button = tkinter.Button(
            self.button_frame, text='Quit', command=self.main_window.destroy)
        self.avg_button.pack(side='left')
        self.sum_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.game1_frame.pack()
        self.game2_frame.pack()
        self.game3_frame.pack()
        self.average_frame.pack()
        self.sum_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()


game_avg = GameAvg()
