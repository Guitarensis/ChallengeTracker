import tkinter as tk
import psutil
from scapy.sendrecv import sniff
from tkinter import messagebox
from dictionary import data_frames, stats_dataframe
from carcombo import selected_car
from geardropdownframe import selected_gear_ratio
import configparser
import requests
import time
from statsframe import StatsWidget, StatsFrame


app_list = ['1320v200.exe', '1320v200Scalable.exe', '1320v200Scalable60.exe']

def check_app_running(app_list):
    for proc in psutil.process_iter(['name']):
        if any(app in proc.info['name'] for app in app_list):
            return True
    print(f"Errno: {' '.join(app_list)} is not running. Please start it.")
    return False

global races_ran, fouls_ran
races_ran = 0
fouls_ran = 0

stats = f'selected_car[selected_gear_ratio][gear_ratio_stats][gear_ratio_stats_extended].json'

if selected_gear_ratio in selected_car:
    race_data = selected_car[selected_gear_ratio]stats_dataframe()
else:
    race_data = selected_car[gear_ratios][gear_ratio_stats][gear_ratio_stats_extended]

def process():
    try:
        try:
            # Define the filter to capture only HTTP traffic from the specified IP address
            filter_str = "host 112.213.36.217 and tcp port 80 and tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420"
            print('filter set to capture packets only from nitto')
        except Exception:
            raise ValueError(f'Error: cant set filter to capture http traffic from nitto ip')
        try:
            # Start capturing packets
            packets = sniff(filter=filter_str, prn=process_packet, store=0)
            print(f"Capturing {len(packets)} packets")
        except Exception:
            raise ValueError(f'Error: Theres some issue capturing packets check network, ip, are they encrypted?')
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
	
    # Initialize the configparser object
    config = configparser.ConfigParser()

    # Get user input for username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Add the user input to the config object
    config['DEFAULT'] = {'username': username, 'password': password}

    # Write the config object to a config.ini file
    with open('scripts', 'config.ini', 'w') as configfile:
        config.write(configfile)

    def display_stats(reaction_time, elapsed_time, bracket_time):

        # Read the API url from config.ini file
        config.read('config.ini')
        username = config['DEFAULT']['username']
        password = config['DEFAULT']['password']

        time.sleep(15)
        # Make a GET request to the API
        url = f"http://toga-barcode.bnr.la/api/Stats/GetPreviousRaceAndRatios?username={username}&password={password}"
        response = requests.get(url)

        if response.status_code == 200:
            # Extract relevant data from the response
            data = response.json()
            elapsed_time = data['et']  # elapsed time is how fast vehicle went down the track
            bracket_time = data['dialin']  # Bracket time is how fast the vehicle was supposed to go down the track
            reaction_time = data['rt']  # Reaction time is how fast the vehicle reacted to the light
            mph = int(round(1320 / elapsed_time * 0.681818, 2))  # calculate mph from elapsed time
            rt_diff = reaction_time - 0.500
            et_diff = elapsed_time - bracket_time

            if reaction_time == -1:
                StatsWidget().update_stats(fouls_ran)
            else:
                StatsWidget().update_stats(mph, rt_diff, et_diff)
        # Run the window
        window.mainloop()
