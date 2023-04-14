import tkinter as tk


class StatsWidget(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.avg_rt_widget = tk.Label(self, text="Avg RT")
        self.avg_rt_widget.grid(row=0, column=0)

        self.avg_rt_display = tk.Label(self)
        self.avg_rt_display.grid(row=0, column=1)

        self.avg_et_widget = tk.Label(self, text="Avg ET")
        self.avg_et_widget.grid(row=1, column=0)

        self.avg_et_display = tk.Label(self)
        self.avg_et_display.grid(row=1, column=1)

        self.avg_mph_widget = tk.Label(self, text="Avg MPH")
        self.avg_mph_widget.grid(row=2, column=0)

        self.avg_mph_display = tk.Label(self)
        self.avg_mph_display.grid(row=2, column=1)

        self.rt_diff_widget = tk.Label(self, text="RT Diff")
        self.rt_diff_widget.grid(row=3, column=0)

        self.rt_diff_display = tk.Label(self)
        self.rt_diff_display.grid(row=3, column=1)

        self.et_diff_widget = tk.Label(self, text="ET Diff")
        self.et_diff_widget.grid(row=4, column=0)

        self.et_diff_display = tk.Label(self)
        self.et_diff_display.grid(row=4, column=1)

        self.et_diff_label = tk.Label(self, text="ET Diff Label")
        self.et_diff_label.grid(row=4, column=2)

        self.rt_diff_label = tk.Label(self, text="RT Diff Label")
        self.rt_diff_label.grid(row=3, column=2)

        self.avg_mph_label = tk.Label(self, text="Avg MPH Label")
        self.avg_mph_label.grid(row=2, column=2)

        self.avg_et_label = tk.Label(self, text="Avg ET Label")
        self.avg_et_label.grid(row=1, column=2)

        self.avg_rt_label = tk.Label(self, text="Avg RT Label")
        self.avg_rt_label.grid(row=0, column=2)

        self.total_races_widget = tk.Label(self, text="Total Races")
        self.total_races_widget.grid(row=5, column=0)

        self.total_races_display = tk.Label(self)
        self.total_races_display.grid(row=5, column=1)

        self.total_races_label = tk.Label(self, text="Total Races Label")
        self.total_races_label.grid(row=5, column=2)

        self.fouls_ran_widget = tk.Label(self, text="Foul Output")
        self.fouls_ran_widget.grid(row=6, column=0)

        self.fouls_ran_display = tk.Label(self)
        self.fouls_ran_display.grid(row=6, column=1)

        self.fouls_ran_label = tk.Label(self, text="Foul Output Label")
        self.fouls_ran_label.grid(row=6, column=2)
