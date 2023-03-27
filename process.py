from datapath import data_folder
from main import car_dropdown, gear_menu_var, root
from savestats import save_stats
from scapy.all import sniff
from scapy.layers.inet import TCP
from tkinter import messagebox
import json
import os
import re

name = 'pSilos Nitto Challenge Stats Tracker'

def process_packet(packet):
    global selected_car, gear_ratio_data, avg_rt, avg_et, avg_mph, avg_rt_output, avg_et_output, avg_mph_output

    payload = str(packet[TCP].payload)

    # Check if the payload contains the expected GET request
    if "GET /gamecode152" not in payload:
        return

    # Extract the required fields from the payload
    match = re.search(r"Reaction Time: (\d+\.\d+).*Estimated Time: (\d+\.\d+).*Trap Speed: (\d+\.\d+).*Bracket Time: (\d+\.\d+).*Whine Data: (\d+\.\d+)", payload)
    if not match:
        raise ValueError('Nothing found in packets')

    reaction_time = float(match.group(1))
    estimated_time = float(match.group(2))
    trap_speed = float(match.group(3))
    bracket_time = float(match.group(4))
    whine_data = float(match.group(5))

    # Get the selected car and gear ratio set
    selected_car = car_dropdown.get()[:-5]
    gear_ratio_set = gear_menu_var.get()

    # Load the stats for the selected car from the corresponding JSON file
    car_file = os.path.join(data_folder, f'{selected_car}.json')
    if not os.path.exists(car_file):
        messagebox.showerror('Error', f'{selected_car} does not exist')
        return
    with open(car_file, 'r') as f:
        car_data = json.load(f)

    # Add the current race stats to the car_data dictionary
    race_stats = {
        'reaction_time': reaction_time,
        'estimated_time': estimated_time,
        'trap_speed': trap_speed,
        'bracket_time': bracket_time,
        'gear_ratio_set': gear_ratio_set,
        'whine_data': whine_data
    }
    car_data['races'].append(race_stats)

    # Save the updated car_data dictionary to the JSON file
    with open(car_file, 'w') as f:
        json.dump(car_data, f)

    # Save the global statistics dictionary to the JSON file
    save_stats()

    # Show success message
    messagebox.showinfo('Success', f'Stats for {selected_car} saved')

    # Calculate and display the average stats
    with open(car_file) as f:
        json_data = json.load(f)
    stats = json_data[gear_ratio_set]['stats']

    total_rt = sum([s['rt'] for s in stats if s['rt'] >= 0.5])
    total_et = sum([s['et'] for s in stats if s['et'] >= 4.37])
    total_mph = sum([s['mph'] for s in stats if s['mph'] >= 0])
    matches_played = len(stats)

    if matches_played > 0:
        avg_rt = round(total_rt / matches_played, 3)
        avg_et = round(total_et / matches_played, 3)
        avg_mph = round(total_mph / matches_played, 2)
    else:
        avg_rt, avg_et, avg_mph = 0, 0, 0

        avg_rt_output.config(state='normal')
        avg_rt_output.delete(0, 'end')
        avg_rt_output.insert(0, avg_rt)
        avg_rt_output.config(state='disabled')
        
        avg_et_output.config(state='normal')
        avg_et_output.delete(0, 'end')
        avg_et_output.insert(0, avg_et)
        avg_et_output.config(state='disabled')

        avg_mph_output.config(state='normal')
        avg_mph_output.delete(0, 'end')
        avg_mph_output.insert(0, avg_mph)
        avg_mph_output.config(state='disabled')

        # Update the gear ratio data dictionary with the current race stats
        if selected_car not in gear_ratio_data:
            gear_ratio_data[selected_car] = {}
        if gear_ratio_set not in gear_ratio_data[selected_car]:
            gear_ratio_data[selected_car][gear_ratio_set] = {
                'matches_played': 0,
                'total_rt': 0,
                'total_et': 0,
                'total_mph': 0
            }
        gear_ratio_data[selected_car][gear_ratio_set]['matches_played'] += 1
        gear_ratio_data[selected_car][gear_ratio_set]['total_rt'] += float(reaction_time)
        gear_ratio_data[selected_car][gear_ratio_set]['total_et'] += float(estimated_time)
        gear_ratio_data[selected_car][gear_ratio_set]['total_mph'] += float(trap_speed)

        # Update the gear ratio data in the corresponding JSON file
        gear_ratio_file = os.path.join(data_folder, 'gear_ratios.json')
        with open(gear_ratio_file, 'w') as f:
            json.dump(gear_ratio_data, f)

        # Update the main window with the current race stats
        root.show_stats()

    if name == 'main':
        sniff(filter='tcp', prn=process_packet, store=0)
