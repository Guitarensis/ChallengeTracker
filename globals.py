import os
import tkinter as tk
from root import root

gear_entries = []
expected_et_entry = None

global avg_rt_output, avg_et_output, avg_mph_output, avg_rt, avg_et, avg_mph

avg_rt_output = tk.Entry(root, state='disabled')
avg_et_output = tk.Entry(root, state='disabled')
avg_mph_output = tk.Entry(root, state='disabled')

app_dir = os.path.dirname(os.path.abspath(__file__))  # get the directory of the current script

cars_dir = os.path.join(app_dir, 'cars')  # the directory containing the JSON files for each car

car_name = {"challenger",
            "charger",
            "civic",
            "ftype",
            "funnycar",
            "lancer",
            "mopar",
            "mustang",
            "ram",
            "rsx",
            "rx8",
            "skyline",
            "srt4",
            "subaru",
            "supra",
            "tfd",
            "viper"}
