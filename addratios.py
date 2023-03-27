from main import gear_entries, gear_menu_var, gear_options, gear_ratio_dropdown, validate, car_dropdown
from dictionary import gear_ratios
import json
import os
from root import root
import sys
from tkinter import messagebox
import tkinter as tk

selected_car = car_dropdown.get()

def add_ratio(gear_ratios, gear_entries):
    global car_dropdown
    if os.path.exists(os.path.join(selected_car, f'{selected_car}.json')):
        with open(os.path.join(f'{selected_car}.json'), 'r') as f:
            json_data = json.load(f)

        if 'gear_ratios' in json_data:
            ratios = json_data['gear_ratios']
            for i in range(1, 7):
                gear_ratio = ratios.get(f'gear{i}')
                if gear_ratio is not None:
                    gear_ratios[f'gear{i}'] = float(gear_ratio)
                    gear_ratio_dropdown['Select Gear'].entryconfig(i, label=f'Gear {i} Ratio: {gear_ratios[f"gear{i}"]}')
        else:
            gear_ratios = {
                'gear1': 0,
                'gear2': 0,
                'gear3': 0,
                'gear4': 0,
                'gear5': 0,
                'gear6': 0,
                'final': 0,
            }

        # Get the selected gear ratio set
        selected_gear_set = gear_menu_var.get()

        # Update gear_ratios with the selected gear ratio
        gear, ratio = gear_entries[0].get().split(':')
        gear_ratios[gear] = float(ratio)

        # Update the car_data dictionary with the new gear ratios
        if 'gear_ratios' in json_data:
            json_data[selected_car]['gear_ratios'] = gear_ratios
        else:
            json_data[selected_car] = {'gear_ratios': gear_ratios}
    
        gear_ratio_dropdown['menu'].delete(0, 'end')
        for option in gear_options[selected_gear_set]:
            gear_ratio_dropdown['menu'].add_command(label=option, command=tk._setit(gear_ratio_dropdown, option))

# Ensure input values are correct.
def validate_ratio():
    # Validate the gear ratios
    for i, gear_entry in enumerate(gear_entries):
        if not validate(gear_entry.get().split(':')[1]):
            messagebox.showerror('Error', f'Gear {i+1} ratio must be a number between 0.5 and 8.0')
            return

    # Update the gear ratio entry fields with the new values.
    for i, gear_entry in enumerate(gear_entries):
        gear_entry.delete(0, 'end')
        gear_entry.insert(0, str(gear_ratios[f'gear{i+1}']))

# Ensure input is correct for final drive.
def validate_final(final):
    try:
        final = float(final)
        if not (2.0 <= final <= 8.0):
            messagebox.showerror('Error', 'Final drive ratio must be a number between 2.0 and 8.0')
            return False
    except ValueError:
        messagebox.showerror('Error', 'Final drive ratio must be a number between 2.0 and 8.0')
        return False
    return True   

def validate_et_entry(expected_et_entry):
    try:
        expected_et = float(expected_et_entry)
        if not (4.37 <= expected_et <= 25):
            return False
    except ValueError:
        return False
    return True

def update_ratios(selected_car):
    global selected_gear_set
    if selected_car is None:
                messagebox.showerror("Error", "Invalid selected car")
                return None

    if selected_gear_set not in selected_car['ratios']:
                messagebox.showerror("Error", f"{selected_car} does not have {selected_gear_set} set")
                return None
        
                ratios = car_data[selected_car]['ratios'][f'gear_ratio_set_{number}']
 
def update_ratio_var(value):
    try:
        return value
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
    messagebox.showerror("Error", f"An error occurred in {__file__} at line {exc_tb.tb_lineno}: {e}")

    def gear_menu():
        gear_menu_var = tk.StringVar(root)
        gear_menu_var.set('Select Gear')

        try:
            gear_menu = tk.OptionMenu(None, gear_menu_var, *gear_options)
        except tk.TclError as e:
            messagebox.showerror("Error", f"An error occurred while creating the OptionMenu: {e}")
            gear_menu = None