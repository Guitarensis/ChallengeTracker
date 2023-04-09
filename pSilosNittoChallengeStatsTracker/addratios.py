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

class AddRatiosWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
    def add_ratio_button(self):
        self.add_ratios_button = QtWidgets.QPushButton(self.mainmenu)
        self.add_ratios_button.setGeometry(QtCore.QRect(510, 320, 75, 23))
        self.add_ratios_button.setObjectName("add_ratios_button")
        self.add_ratios_button.clicked.connect(lambda: add_ratios(selected_car, gear_ratios_df, final_ratio_df,
                                                                  gear_ratio_set))
        return add_ratios()`1