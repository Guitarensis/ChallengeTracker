from carcombo import selected_car
from globals import dictionary_file
import json
import os
import pandas as pd

def load_gear_ratios(selected_car):
    car_file = f'cars/{selected_car}.json'

    # Check if the car file exists and is not empty
    if os.path.exists(car_file) and os.path.getsize(car_file) > 0:
        with open(car_file, 'r') as f:
            data = json.load(f)
            return data["gear_ratios"]
    else:
        # Populate car JSON file with data from dictionary.py
        dictionary = pd.read_csv(
        dictionary_file, delimiter="=", header=None, names=["key", "value"], index_col="key"
                )
        data = {"gear_ratios": dictionary.loc[selected_car].to_dict()}
        with open(car_file, 'w') as f:
            json.dump(data, f)

        # Load car JSON file into memory
        with open(car_file, 'r') as f:
            data = json.load(f)
            return data["gear_ratios"]