from globals import expected_et_entry
from root import root
from tkinter import messagebox
from tkinter import tk
import psutil
import psutil
import tkinter.ttk as ttk


def check_app_running(app_name):
    for proc in psutil.process_iter(['name']):
        if app_name in proc.info['name']:
            return True
    return False

def check_required_apps():
    # Check if the required apps are running
    required_apps = ['1320v200Scalable60.exe', '1320v200Scalable.exe', '1320v200.exe']
    for app in required_apps:
        if not check_app_running(app):
            messagebox.showerror("Error", f"{app} is not running. Please start it.")
            return False
    return True

# Create labels and entry fields for average RT, ET, and MPH
avg_rt_label = tk.Label(root, text='Average RT:')
avg_rt_output = tk.Entry(root, state='disabled')
avg_rt_label.grid(row=4, column=0)
avg_rt_output.grid(row=4, column=1)

avg_et_label = tk.Label(root, text='Average ET:')
avg_et_output = tk.Entry(root, state='disabled')
avg_et_label.grid(row=5, column=0)
avg_et_output.grid(row=5, column=1)

avg_mph_label = tk.Label(root, text='Average MPH:')
avg_mph_output = tk.Entry(root, state='disabled')
avg_mph_label.grid(row=6, column=0)
avg_mph_output.grid(row=6, column=1)
print('Average RT, ET, and MPH labels and entries created')

rt_diff_label = tk.Label(root, text='RT diff:')
rt_diff_output = tk.Entry(root, state='disabled')
rt_diff_label.grid(row=7, column=0)
rt_diff_output.grid(row=7, column=1)

dial_in_label = tk.Label(root, text='RT diff:')
dial_in_output = tk.Entry(root)
dial_in_label.grid(row=8, column=0)
dial_in_output.grid(row=8, column=1)
print('RT diff and dial in labels and entries created')

et_diff_label = tk.Label(root, text='ET dial in diff:')
et_diff_output = tk.Entry(root, state='disabled')
et_diff_label.grid(row=9, column=0)
et_diff_output.grid(row=9, column=1)
print('ET dial in diff label and entry created')

# create labels and entries
fouls_label = tk.Label(root, text='fouls')
fouls_output = tk.Entry(root, state='disabled')
races_label = tk.Label(root, text='races')
races_output = tk.Entry(root, state='disabled')
races_label.grid(row=0, column=0, padx=(0, 5))
races_output.grid(row=0, column=1, padx=(0, 20))
fouls_label.grid(row=0, column=2)
fouls_output.grid(row=0, column=3, padx=(0, 5))
print('Fouls and races labels and entries created')

gear_options = ["Select Gear", "Gear1", "Gear2", "Gear3", "Gear4", "Gear5", "Gear6", "Final", "Expected ET"]

# Create labels and entry fields for gear ratios
gear_menu_var = tk.StringVar()
gear_menu_var.set("Select Gear Set")
gear_ratios_label = tk.Label(root, text='Add Gear Ratios:')
gear_ratios_label.grid(row=1, column=2)
gear_ratio_dropdown = ttk.Combobox(root)
gear_ratio_dropdown.set("Select Gear Set")
gear_ratio_dropdown.grid(row=2, column=2)

gear_entries = []
for i in range(6):
    gear_label = tk.Label(root, text=f'Gear {i+1}:')
    gear_entry = tk.Entry(root)
    gear_label.grid(row=i+3, column=3)
    gear_entry.grid(row=i+3, column=4)
    print('Created entry fields for gear ratios')

# Create labels and entry fields for the final gear ratio and expected ET
final_label = tk.Label(root, text='Final Gear Ratio:')
final_entry = tk.Entry(root)
expected_et_label = tk.Label(root, text='Expected ET of Ratio Set:')
expected_et_entry = tk.Entry(root)

# Pack the labels, entry fields, and submit button in the window
final_label.grid(row=9, column=0)
final_entry.grid(row=9, column=1)
expected_et_label.grid(row=10, column=0)
expected_et_entry.grid(row=10, column=1)
print('final and expected et fields created and packed')
