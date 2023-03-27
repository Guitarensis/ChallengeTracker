from globals import avg_et_output, avg_mph_output, avg_rt_output, root
from tkinter import messagebox
import json

def clear_stats():
    global total_rt, total_et, total_mph, matches_played, json_data, selected_car
    file_path = f'{selected_car}.json'
    with open(file_path) as f:
        json_data = json.load(f)
    confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all data?")
    if confirmed:
        # Clear the stats from the JSON file
        json_data['stats'] = []
        json_data['ratios'] = []
        json_data['matches_played'] = 0
        with open(file_path, 'w') as f:
            json.dump(json_data, f)

        total_rt, total_et, total_mph, matches_played = 0, 0, 0, 0

        # Clear average Entry widgets
        avg_rt_output.delete(0, 'end')
        avg_et_output.delete(0, 'end')
        avg_mph_output.delete(0, 'end')

        # Reset global variables
        total_rt = 0.000
        total_et = 00.000
        total_mph = 000.00
        matches_played = 0
    
        messagebox.showinfo('Stats Cleared', 'All stats have been cleared.')

clear_button = tk.Button(root, text='Clear Stats', command=clear_stats)
clear_button.grid(row=4, column=11)

root.mainloop()