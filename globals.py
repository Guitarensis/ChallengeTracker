import os

# globals
import tkinter as tk

root = tk.Tk()
gear_entries = []
expected_et_entry = None
import tkinter as tk

root = tk.Tk()

global avg_rt_output
avg_rt_output = tk.Entry(root, state='disabled')

global avg_et_output
avg_et_output = tk.Entry(root, state='disabled')

global avg_mph_output
avg_mph_output = tk.Entry(root, state='disabled')

app_dir = os.path.dirname(os.path.abspath(__file__))  # get the directory of the current script

cars_dir = os.path.join(app_dir, 'cars')  # the directory containing the JSON files for each car