from carcombo import selected_car
from datetime import time
from dictionary import gear_ratio_stats_df, gear_ratio_stats_extended_df, gear_ratio_stats
from gearwidget import selected_gear_ratio
from statswidget import avg_rt_widget, avg_et_widget, avg_mph_widget, mph_diff_widget, rt_diff_widget, et_diff_widget, foul_output_widget, races_ran_widget, total_races_widget
import datetime
import json
import os
import pandas as pd
import requests
import configparser

df = f'cars/{selected_car}.json'

data_dir = 'cars/'

dfs = {}
for file_name in os.listdir(data_dir):
    if file_name.endswith('.json'):
        with open(os.path.join(data_dir, file_name)) as f:
            data = json.load(f)
            df = pd.DataFrame(data)
            key = file_name[:-5]  # remove '.json' extension from key
            dfs[key] = df

def process_packet(gear_ratio_set):

    with open(df) as f:
        data = json.load(f)
        df = pd.DataFrame(data)

    try:
        # Check if selected_gear_ratio is None
        if selected_gear_ratio is None:
            # Ask user to input gear ratios and select them in dropdown
            print('add some ratios to the car first')
        else:
            # Use selected_gear_ratio from dropdown
            gear_ratio = selected_gear_ratio

    except Exception:
        raise ValueError("Invalid gear ratios")

    # Initialize the configparser object
    config = configparser.ConfigParser()

    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Add the user input to the config object
    config['DEFAULT'] = {'username': username, 'password': password}

    # Write the config object to a config.ini file
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    # Read the API url from config.ini file
    config.read('config.ini')
    username = config['DEFAULT']['username']
    password = config['DEFAULT']['password']
    url = f"http://toga-barcode.bnr.la/api/Stats/GetPreviousRaceAndRatios?username={username}&password={password}"

    time.sleep(15)
    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract relevant data from the response
        data = response.json()
        elapsed_time = data(int(round['et', 00.000]))
        bracket_time = data(int(round['dialin', 00,000]))
        reaction_time = data(int(round['rt', 0.000]))
        mph = int(round(1320/elapsed_time * 0.681818, 2))
        gear_ratio_stats = gear_ratio_stats_df.loc[gear_ratio_set]
        df.at[gear_ratio_set, 'rt'] = gear_ratio_stats[1]
        df.at[gear_ratio_set, 'et'] = gear_ratio_stats[3]
        df.at[gear_ratio_set, 'mph'] = gear_ratio_stats[5]

        # Grab mph and elapsed time from last two races of current car
        last_two_races = df[df['car'] == selected_car].tail(2)
        mph = last_two_races['mph'].tolist()
        race_times = last_two_races['race_time'].tolist()

        # Calculate the elapsed time in seconds for each race
        elapsed_times = []
        for time in race_times:
            time_seconds = datetime.strptime(time, '%M:%S.%f')
            elapsed_time = (time_seconds - datetime(1900, 1, 1)).total_seconds()
            elapsed_times.append(elapsed_time)

        # Calculate the average elapsed time
        avg_elapsed_time = sum(elapsed_times) / len(elapsed_times)

        # Update the widgets with relevant data
        if reaction_time == -1:
            reaction_type = "Foul"
        else:
            reaction_type = "RT"
            reaction_type = foul_output_widget
            avg_rt_widget.value = str(int(reaction_time)) + " " + reaction_type
            avg_et_widget.value = str(int(avg_elapsed_time))
            avg_mph_widget.value = str(int(mph.mean()))
            et_diff_widget.value = str(int(bracket_time - avg_elapsed_time)) # Calculate and display et difference
            rt_diff_widget.value = str(round(reaction_time - 0.5, 3)) # Calculate and display rt difference from .500
            mph_diff_widget.value = str(int(sum(elapsed_times) / len(elapsed_times)))


def update_fouls(foul, packet, races_ran):
    # Extract the foul flag, and number of races ran from the packet
    foul = packet['Foul']
    races_ran = packet['racesran']

    # Update the gear ratio stats for the current packet
    df = df.append({'gear_ratio_set': gear_ratio_set, 'fouls': foul, 'racesran': races_ran}, ignore_index=True)

    max_races = max(gear_ratio_stats_extended.items(), key=lambda x: x[3])[3]
    for gear_ratio, stats in gear_ratio_stats_extended.items():
        if stats[3] >= max_races:
            # Update the current max races and corresponding gear ratio set number
            max_races = stats[3]
            max_races_gear_ratio = gear_ratio

    # Return the gear ratio set number with the most races
    return max_races_gear_ratio

# Update the number of fouls and races ran for the specified gear ratio set
gear_ratio_stats_extended_df.at[gear_ratio_set, 'fouls']
gear_ratio_stats_extended_df.at[gear_ratio_set, 'racesran']

# Update the corresponding DataFrame
gear_ratio_stats_extended = gear_ratio_stats_extended_df.loc[gear_ratio_set]
df.at[gear_ratio_set, 'rtdiff'] = gear_ratio_stats[7]
df.at[gear_ratio_set, 'etdiff'] = gear_ratio_stats[9]
df.at[gear_ratio_set, 'mphdiff'] = gear_ratio_stats[11]
df.at[gear_ratio_set, 'fouls'] = gear_ratio_stats_extended[1]
df.at[gear_ratio_set, 'racesran'] = gear_ratio_stats_extended[3]
# Update the foul output widget with the current number of fouls
foul_output_widget.config(text=f"fouls: {selected_car[gear_ratio_stats_extended][gear_ratio_set][1]}")

# Update the races ran widget with the current number of races ran
races_ran_widget.config(text=f"races Ran: {selected_car[gear_ratio_stats_extended][gear_ratio_set][3]}")

def total_races():
    # Get the list of all JSON files in the cars folder
    cars_folder = 'cars'
    json_files = [f for f in os.listdir(cars_folder) if f.endswith('.json')]

    total_races = 0

    # Loop through each JSON file and add the number of races to the total
    for json_file in json_files:
        with open(os.path.join(cars_folder, json_file)) as f:
            data = json.load(f)
            for gear_ratio_set in data['gear_ratio_stats_extended']:
                total_races += gear_ratio_set[3]

    # Add the number of races in the dataframes in memory to the total
    for df in [gear_ratio_stats_df, gear_ratio_stats_extended_df]:  # replace with your actual dataframe names
        total_races += len(df)

    # Update the total races widget
    total_races_widget.config(text=f"Total Races: {0}")
