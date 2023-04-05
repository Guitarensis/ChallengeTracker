from carlist import car_dropdown
from main import root, gear_menu_var
from process import process_packet
from tkinter import messagebox, tk 
import json
import os

def races_ran():
    # Get the selected car and gear ratio set
    car_dropdown.get()
    gear_menu_var.get()

    # Add race count to the car's stats
    os.path.join(data_folder, f'{car_dropdown.get()}.json')
    if not os.path.exists(car_file):
        messagebox.showerror('Error', f'{car_dropdown.get()} does not exist')
        return
    with open(car_file, 'r') as f:
        car_data = json.load(f)
    if 'races_ran' not in car_data:
        car_data['races_ran'] = {}
    if gear_menu_var not in car_data['races_ran']:
        car_data['races_ran'][gear_menu_var.get()] = 0
    car_data['races_ran'][gear_menu_var.get()] += 1

    # Save the updated car_data dictionary to the JSON file
    with open(car_file, 'w') as f:
        json.dump(car_data, f)

    # Update races ran output
    races_ran_output.configure(state='normal')
    races_ran_output.delete(0, tk.END)
    races_ran_output.insert(0, car_data['races_ran'][gear_menu_var]
    races_ran_output.configure(state='disabled')
    races_ran_label.configure(text=f'Races ran with {car_dropdown.get} and {gear_menu_var}:')
