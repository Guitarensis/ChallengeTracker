import threading
import time
from dictionary import gear_ratio_set, gear_ratio_stats_extended_df


from loaddataframes import load_dataframes
# Define the interval for auto-dumping data to files in seconds
DUMP_INTERVAL = 900
# 15 minutes

# Define a function to periodically dump all dataframes to JSON files


def auto_dump_dataframes(dataframes, selected_car, selected_gear_ratio):
    while True:
        dump_dataframes(selected_car, selected_gear_ratio, dataframes)
        time.sleep(DUMP_INTERVAL)
        try:
            # Start a separate thread to periodically dump dataframes
            threading.Thread(target=auto_dump_dataframes, daemon=True).start()
        except Exception:
            raise ValueError('Error starting thread to dump data every 15.')

        # Define the gear ratio dictionaries
        gear_ratio_stats_df.loc[gear_ratio_set]
        gear_ratio_stats_extended_df.loc[gear_ratio_set]

        # Dump the data to a file
        for car, df in dataframes.items():
            df.to_json(f'cars/{car}.json', index=False)
