from carcombo import selected_car
from dictionary import gear_ratios, gear_ratio_set, gear_ratio_stats, gear_ratio_stats_extended, final_ratio
from gearwidget import GearsWidget
import pandas as pd

# define the save_df function
def save_df(filename):
    filename = f"cars/{selected_car}.json"
    with open(filename, 'w') as f:
            f.write(df.to_json())
    # combine the gear ratios and final ratio/expected ET DataFrames
    df = pd.concat([pd.DataFrame(columns=selected_car[gear_ratios][gear_ratio_set], index=[0]),
                pd.DataFrame(columns=selected_car[final_ratio]['final_drive'], ['expected_et'], index=[0]),
                pd.DataFrame(columns=selected_car[gear_ratios][gear_ratio_set][gear_ratio_stats]),
                pd.DataFrame(columns=selected_car[gear_ratios][gear_ratio_set][gear_ratio_stats][gear_ratio_stats_extended])],
               axis=1)

    # save the DataFrame to a json
    df.to_json('filename', index=False)

    # add a new row with the user input values
    df.loc[0] = [selected_car, GearsWidget.gear_1_entry.text(), GearsWidget.gear_2_entry.text(), GearsWidget.gear_3_entry.text(),
                 GearsWidget.gear_4_entry.text(), GearsWidget.gear_5_entry.text(), GearsWidget.gear_6_entry.text(),
                 GearsWidget.final_entry.text(), GearsWidget.expected_et_entry.text()]

