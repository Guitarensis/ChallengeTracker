import tkinter as messagebox
from globals import gear_entries, expected_et_entry
from dictionary import gear_ratios

# Ensure input values are correct.
def validate_ratio():
    global root
    # Validate the gear ratios
    for i, gear_entry in enumerate(gear_entries):
        if not validate_ratio(gear_entry.get().split(':')[1]):
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
    finally:
        return False
    return True

def validate_et(et):
    try:
        expected_et_entry = float(et)
        if not (4.37 <= et <= 25):
            messagebox.showerror('Error', 'Expected ET is the max et for your ratio set')
            return False
    except ValueError:
        return False
    return True
