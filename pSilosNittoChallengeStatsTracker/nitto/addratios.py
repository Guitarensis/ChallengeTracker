import itertools
import pandas as pd
from carcombo import CarsWidget
from datas import dataframes


# Function to save dataframes to disk
def auto_dump_dataframes(dataframes, selected_car, **kwargs):
    for selected_car, df in dataframes.items():
        file_name = f"cars/{selected_car}.json"
        with open(file_name, "r+") as f:
            data = json.load(f)
            data[df_name] = json.loads(df.to_json())
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

# Function to generate gear ratio combinations
def generate_gear_ratio_combinations(dataframes):
    # Generate a list of gear ratio sets
    gear_ratio_sets = selected_car(dataframes.index.tolist())

    # Initialize an empty list to hold the gear ratio combinations
    gear_ratio_combo = []

    # Iterate over each gear ratio set
    for gear_ratio_set in gear_ratio_sets:

        # Get the gear ratios for the current gear ratio set
        gear_ratios = gear_ratios_df.loc[gear_ratio_set].tolist(),
        final_ratio = final_ratio_df.loc[gear_ratio_set].tolist()


        # Generate all possible combinations of gear ratios
        combinations = list(itertools.combinations(gear_ratios, 2))

        # Append the gear ratio combinations to the gear_ratio_combo list
        gear_ratio_combo.extend(combinations)


def add_ratios(selected_car, final_entry, expected_et_entry):
    """
    This function takes user inputs from the gear ratio entry fields, final drive and expected et and adds them to the
    dataframe loaded in memory according to selected car and saves them to cars/{selected_car}.json file inside dictionary
    gear_ratios as gear_ratio_set_{numberhere}
    """
    # Load the gear ratios dataframe
    gear_ratios_df = dataframes[selected_car]

    # Load the final ratio dataframe
    final_ratio_df = dataframes[selected_car]

    # Generate the gear ratio combinations
    generate_gear_ratio_combinations()

    # Save the updated dataframes to disk
    auto_dump_dataframes(selected_car(dataframes))

def add_ratio_button():
    self.add_ratios_button = QtWidgets.QPushButton(self.mainmenu)
    self.add_ratios_button.setGeometry(QtCore.QRect(510, 320, 75, 23))
    self.add_ratios_button.setObjectName("add_ratios_button")
    self.add_ratios_button.clicked.connect(lambda: add_ratios(dataframes[selected_car]))
    return add_ratios()