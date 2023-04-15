import json
import tkinter as tk
from tkinter import ttk
from cardataframes import dataframes
from dictionary import gear_ratio_set, gear_ratios_df, final_ratio_df
from geardropdown import gear_ratio_combo


# Function to save dataframes to disk
def auto_dump_dataframes(dataframes, selected_car, **kwargs):
    df_name = selected_car
    for selected_car, df in dataframes.items():
        file_name = f"cars/{selected_car}.json"
        with open(file_name, "r+") as file:
            data = json.load(file)
            data[df_name] = json.loads(df.to_json())
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()


def add_ratios(selected_car, gear_ratios_df, final_ratio_df, gear_ratio_set):
    """
    This function takes user inputs from the gear ratio entry fields, final drive and expected et and adds them to the
    dataframe loaded in memory according to selected car and saves them to cars/{selected_car}.json file inside dictionary
    gear_ratios as gear_ratio_set_{numberhere}
    """
    # Load the gear ratios dataframe
    dataframes[selected_car + "_df"] = pd.concat([dataframes[selected_car + "_df"], [gear_ratios_df],
                                                  final_ratio_df], axis=1)

    # Generate the gear ratio combinations
    gear_ratio_combo(gear_ratio_set)

    # Save the updated dataframes to disk
    auto_dump_dataframes(dataframes, selected_car)


class AddRatiosWidget(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.add_ratios_button = ttk.Button(self, text="Add Ratios", command=self.add_ratios)
        self.add_ratios_button.grid(row=0, column=0, padx=10, pady=10)

    def add_ratios(self):
        add_ratios(selected_car, gear_ratios_df, final_ratio_df, gear_ratio_set)


class CarsWidget(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.selected_car = tk.StringVar(value=dataframes.keys()[0])
        
        self.car_combo = ttk.Combobox(self, values=list(dataframes.keys()), textvariable=self.selected_car)
        self.car_combo.grid(row=0, column=0, padx=10, pady=10)
        self.car_combo.bind("<<ComboboxSelected>>", self.update_selected_car)

    def update_selected_car(self, event):
        self.selected_car.set(self.car_combo.get())
