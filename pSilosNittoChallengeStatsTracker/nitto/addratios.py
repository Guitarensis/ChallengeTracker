import itertools
import pandas as pd
from dictionary import gear_ratio_set, gear_ratios_df, final_ratio_df


# Function to save dataframes to disk
def auto_dump_dataframes(car_name, **kwargs):
    for df_name, df in kwargs.items():
        file_name = f"cars/{car_name}.json"
        with open(file_name, "r+") as f:
            data = json.load(f)
            data[df_name] = json.loads(df.to_json())
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

# Function to generate gear ratio combinations
def generate_gear_ratio_combinations():
    global gear_ratio_df, final_ratio_df
    # Generate a list of gear ratio sets
    gear_ratio_sets = gear_ratios_df.index.tolist()

    # Initialize an empty list to hold the gear ratio combinations
    gear_ratio_combo = []

    # Iterate over each gear ratio set
    for gear_ratio_set in gear_ratio_sets:

        # Get the gear ratios for the current gear ratio set
        gear_ratios = gear_ratios_df.loc[gear_ratio_set].tolist()

        # Generate all possible combinations of gear ratios
        combinations = list(itertools.combinations(gear_ratios, 2))

        # Append the gear ratio combinations to the gear_ratio_combo list
        gear_ratio_combo.extend(combinations)

        # Check if the gear_ratio_combo list has 8 entries
        if len(gear_ratio_combo) == 8:
            # Get the final and expectedet values for the current gear ratio set
            final_ratio = final_ratio_df.loc[gear_ratio_set].tolist()

            # Append the final and expectedet values to the gear_ratio_combo list
            gear_ratio_combo.extend(final_ratio[1:])

            # Print the gear ratio combination for the current gear ratio set
            print(f"Gear Ratio Set: {gear_ratio_set}, Gear Ratio Combination: {gear_ratio_combo}")

            # Reset the gear_ratio_combo list for the next gear ratio set
            gear_ratio_combo = []

def add_ratios(selected_car, final_entry, expected_et_entry):
    """
    This function takes user inputs from the gear ratio entry fields, final drive and expected et and adds them to the
    dataframe loaded in memory according to selected car and saves them to cars/{selected_car}.json file inside dictionary
    gear_ratios as gear_ratio_set_{numberhere}
    """

    global gear_ratios_df
    global final_ratio_df
    global gear_ratio_set

    # Load the gear ratios dataframe
    gear_ratios_df = pd.read_json(f"cars/{selected_car}.json", orient="index")

    # Load the final ratio dataframe
    final_ratio_df = pd.read_json(f"cars/{selected_car}.json", orient="index")

    # Generate the gear ratio combinations
    generate_gear_ratio_combinations()

    # Save the updated dataframes to disk
    auto_dump_dataframes(selected_car, gear_ratios_df=gear_ratios_df, final_ratio_df=final_ratio_df)

def add_ratio_button():
    self.add_ratios_button = QtWidgets.QPushButton(self.mainmenu)
    self.add_ratios_button.setGeometry(QtCore.QRect(510, 320, 75, 23))
    self.add_ratios_button.setObjectName("add_ratios_button")
    self.add_ratios_button.clicked.connect(lambda: add_ratios(selected_car))
    return add_ratios()