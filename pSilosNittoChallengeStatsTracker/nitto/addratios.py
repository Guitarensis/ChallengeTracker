import itertools
import pandas as pd
from carcombo import CarsWidget
from cardataframes import dataframes
from dictionary import gear_ratio_set


# Function to save dataframes to disk
def auto_dump_dataframes(dataframes, selected_car, **kwargs):
    df_name = selected_car
    for selected_car, df in dataframes.items(selected_car):
        file_name = f"cars/{selected_car}.json"
        with open(file_name, "r+") as file:
            data = json.load(file)
            data[df_name] = json.loads(df.to_json())
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

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