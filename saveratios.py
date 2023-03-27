from main import gear_entries, gear_menu_var, gear_ratio_dropdown, gear_options, final_entry
from validate import validate_et
import json
import os
import tkinter as tk
import tkinter as messagebox


# Create a function to save the gear ratios to the car_data dictionary.
def save_ratios(gear_ratios, selected_car):
    global root, expected_et_entry
    # Get the selected car and gear
    selected_gear_set = gear_menu_var.get()

    car_filename = os.path.join(selected_car, f"{selected_car}.json")
    
    if os.path.exists(car_filename):
        with open(car_filename, 'r') as f:
            json_data = json.load(f)
    else:
        json_data = {}

    # Check if the gear ratios for the selected gear set have already been entered
    if 'gear_ratios' in json_data and selected_gear_set in json_data['gear_ratios']:
        messagebox.showerror('Error', f'Gear ratios for {selected_car} and {selected_gear_set} already exist')
        return
    
    try:
        # Get the gear ratios from the entry boxes
        gear1, gear2, gear3, gear4, gear5, gear6 = [gear_entry.get().split(':')[1] for gear_entry in gear_entries]
        final = final_entry.get()
        expected_et_entry.get()
        print('got ratios from entry box')
    except ValueError:
        print('couldnt get the ratios from entry boxes')
        
    # Update the car_data dictionary with the entered gear ratios and expected ET
    if 'gear_ratios' in json_data:
        json_data['gear_ratios'].update(gear_ratios)
    else:
        json_data['gear_ratios'] = gear_ratios
    if validate_et(expected_et_entry):
        json_data['expected_et'] = expected_et_entry

    with open(car_filename, 'w') as f:
        json.dump(json_data, f)

    try:
        # Update the gear ratio dropdown menu with the newly added gear ratio set
        gear_options[selected_gear_set] = f'{selected_gear_set}: {gear1}:{gear2}:{gear3}:{gear4}:{gear5}:{gear6}:{final}'
        gear_ratio_dropdown['menu'].add_command(label=gear_options[selected_gear_set], command=tk._setit(gear_ratio_dropdown, gear_options[selected_gear_set]))
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update gear ratio dropdown: {e}")
    try:
        # Create the Add Ratios, Save Stats, and Clear Stats buttons
        add_ratio_button = tk.Button(root, text='Add Ratios', command=lambda: save_ratios(gear_ratios))
        add_ratio_button.grid(row=3, column=11)
        print('Add Ratio button added')
    except Exception as e:
        raise ValueError('Error creating Add Ratio button')
