import os
import pandas as pd
from cardataframes import dataframes, selected_car


gear_ratios_df = None
final_ratio_df = None
gear_ratio_stats_df = None
gear_ratio_stats_extended_df = None
gear_ratio_set = None


def data_frames():
    global gear_ratios_df, final_ratio_df, gear_ratio_stats_df, gear_ratio_stats_extended_df, gear_ratio_set

    gear_ratios = {"gear_ratio_set_1": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_2": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_3": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_4": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_5": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_6": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_7": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_8": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_9": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_10": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_11": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_12": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_13": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_14": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0],
                   "gear_ratio_set_15": ["gear1", 0, "gear2", 0, "gear3", 0, "gear4", 0, "gear5", 0, "gear6", 0]}

    gear_ratios_df = pd.DataFrame.from_dict(gear_ratios, orient='index', columns=["gear1", "entry", "gear2",
                                                                                  "entry", "gear3", "entry",
                                                                                  "gear4", "entry", "gear5",
                                                                                  "entry", "gear6", "entry"])
    gear_ratios_df.set_index('gear1', inplace=True)

    final_ratio = {"gear_ratio_set_1": ["final", 0, "expected", 0],
                   "gear_ratio_set_2": ["final", 0, "expected", 0],
                   "gear_ratio_set_3": ["final", 0, "expected", 0],
                   "gear_ratio_set_4": ["final", 0, "expected", 0],
                   "gear_ratio_set_5": ["final", 0, "expected", 0],
                   "gear_ratio_set_6": ["final", 0, "expected", 0],
                   "gear_ratio_set_7": ["final", 0, "expected", 0],
                   "gear_ratio_set_8": ["final", 0, "expected", 0],
                   "gear_ratio_set_9": ["final", 0, "expected", 0],
                   "gear_ratio_set_10": ["final", 0, "expected", 0],
                   "gear_ratio_set_11": ["final", 0, "expected", 0],
                   "gear_ratio_set_12": ["final", 0, "expected", 0],
                   "gear_ratio_set_13": ["final", 0, "expected", 0],
                   "gear_ratio_set_14": ["final", 0, "expected", 0],
                   "gear_ratio_set_15": ["final", 0, "expected", 0]}

    final_ratio_df = pd.DataFrame. from_dict(final_ratio, orient='index', columns=["final", "entry",
                                                                                   "expected", "entry"])
    final_ratio_df.set_index(['final'], inplace=True)

    gear_ratio_stats = {"gear_ratio_set_1": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                        "gear_ratio_set_2": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                        "gear_ratio_set_3": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                        "gear_ratio_set_4": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                        "gear_ratio_set_5": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                        "gear_ratio_set_6": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                        "gear_ratio_set_7": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                        "gear_ratio_set_8": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                        "gear_ratio_set_9": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                        "gear_ratio_set_10": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff",
                                              0],
                        "gear_ratio_set_11": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff",
                                              0],
                        "gear_ratio_set_12": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff",
                                              0],
                        "gear_ratio_set_13": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff",
                                              0],
                        "gear_ratio_set_14": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff",
                                              0],
                        "gear_ratio_set_15": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff",
                                              0]}

    gear_ratio_stats_df = pd.DataFrame.from_dict(gear_ratio_stats, orient='index', columns=["rt", "entry", "et",
                                                                                            "entry", "mph", "entry",
                                                                                            "rtdiff", "entry",
                                                                                            "etdiff", "entry",
                                                                                            "mphdiff", "entry"])

    gear_ratio_stats_df.set_index(['rt', 'et', 'mph', 'rtdiff', 'etdiff', 'mphdiff'], inplace=True)

    gear_ratio_stats_extended = {"gear_ratio_set_1": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_2": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_3": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_4": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_5": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_6": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_7": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_8": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_9": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_10": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_11": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_12": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_13": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_14": ["fouls", 0, "racesran", 0],
                                 "gear_ratio_set_15": ["fouls", 0, "racesran", 0]}

    gear_ratio_stats_extended_df = pd.DataFrame.from_dict(gear_ratio_stats_extended, orient='index', columns=[
                                "fouls", "entry", "racesran", "entry", 60, "entry", 100, "entry", 330, "entry",
                                660, "entry"])
    gear_ratio_stats_extended_df.set_index(['fouls'], inplace=True)

    return final_ratio_df, gear_ratios_df, gear_ratio_stats_extended_df, gear_ratio_stats_df, gear_ratio_set


data_frames(selected_car)


def load_dataframes():
    for file_name in os.listdir('cars'):
        if file_name.endswith('.json'):
            selected_car = file_name[:-5]
            file_path = os.path.join('cars', file_name)
            data_frames[selected_car+'_df'] = pd.read_json(file_path, encoding='utf-8')
    globals().update(data_frames)


# Function to clear gear ratio set
def clear_gear_ratio_set(gear_ratio_set_name):
    global gear_ratios_df, final_ratio_df, gear_ratio_stats_df, gear_ratio_stats_extended_df, gear_ratio_set
    gear_ratios_df[gear_ratio_set_name] = 0
    final_ratio_df[gear_ratio_set_name] = 0
    gear_ratio_stats_df[gear_ratio_set_name] = 0
    gear_ratio_stats_extended_df[gear_ratio_set_name] = 0

