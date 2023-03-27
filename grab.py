import os
from main import car_dropdown
from global import root
from car_path import *
from tkinter import ttk

selected_car = ""

def get_car():
    selected_car = car_dropdown.get()  # get the currently selected car from the car dropdown
    car_file = f"{selected_car}.json"  # construct the filename of the JSON file for the selected car
    car_path = os.path.join(cars_dir), car_file)  # get the full path to the JSON file for the selected car

    car_names = []
    # loop through the JSON files in the cars directory
    for filename in os.listdir(cars_dir):
        if filename.endswith('.json'):  # only process JSON files
            car_name = os.path.splitext(filename)[0]  # get the name of the car from the filename
            car_names.append(car_name)  # add the car name to the list

    return car_path, car_names  # return the path to the selected car's JSON file and the list of car names

# Call the get_car function to initialize the car dropdown
car_path, car_names = get_car()

# Create the car dropdown
car_dropdown = ttk.Combobox(root, values=car_names)
car_dropdown.set("Select Car")
car_dropdown.grid(row=1, column=2)

# Bind the car dropdown to the get_car function
car_dropdown.bind("<<ComboboxSelected>>", get_car)