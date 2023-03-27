from tkinter import messagebox, tk 
from process import process_packet
from main import root, gear_menu_var, car_dropdown
import json
import os
from path import data_folder

def races_ran():
    global selected_car, selected_gear_set

    # Get the selected car and gear ratio set
    car_dropdown.get()
    selected_gear_set = gear_menu_var.get()

    # Add race count to the car's stats
    car_file = os.path.join(data_folder, f'{selected_car}.json')
    if not os.path.exists(car_file):
        messagebox.showerror('Error', f'{selected_car} does not exist')
        return
    with open(car_file, 'r') as f:
        car_data = json.load(f)
    if 'races_ran' not in car_data:
        car_data['races_ran'] = {}
    if selected_gear_set not in car_data['races_ran']:
        car_data['races_ran'][selected_gear_set] = 0
    car_data['races_ran'][selected_gear_set] += 1

    # Save the updated car_data dictionary to the JSON file
    with open(car_file, 'w') as f:
        json.dump(car_data, f)

    # Update races ran output
    races_ran_output.configure(state='normal')
    races_ran_output.delete(0, tk.END)
    races_ran_output.insert(0, car_data['races_ran'][selected_gear_set])
    races_ran_output.configure(state='disabled')
    races_ran_label.configure(text=f'Races ran with {selected_car} and {selected_gear_set}:')

root.mainloop()