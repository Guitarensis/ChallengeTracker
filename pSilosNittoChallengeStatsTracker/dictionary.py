import os
import pandas as pd
from PyQt5 import QtCore, QtWidgets

gear_ratios_df = None
final_ratio_df = None
gear_ratio_stats_df = None
gear_ratio_stats_extended_df = None
gear_ratio_set = None

def data_frames():
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
    return gear_ratios_df

    final_ratio_df = {"gear_ratio_set_1": ["final", 0, "expected", 0],
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

    final_ratio_df = pd.DataFrame. from_dict(final_ratio_df, orient='index', columns=["final", "entry",
                                                                                      "expected", "entry"])
    final_ratio_df.set_index(['final'], inplace=True)
    return final_ratio_df


def stats_dataframe():
    gear_ratio_stats_df = {"gear_ratio_set_1": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
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

    gear_ratio_stats_df = pd.DataFrame.from_dict(gear_ratio_stats_df, orient='index', columns=["rt", "entry", "et",
                                                                                               "entry", "mph", "entry",
                                                                                               "rtdiff", "entry",
                                                                                               "etdiff", "entry",
                                                                                               "mphdiff", "entry"])
    gear_ratio_stats_df.set_index(['rt', 'et', 'mph', 'rtdiff', 'etdiff', 'mphdiff'], inplace=True)
    return gear_ratio_stats_df


def stats_extended():
        gear_ratio_stats_extended_df = {"gear_ratio_set_1": ["fouls", 0, "racesran", 0],
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

        gear_ratio_stats_extended_df = pd.DataFrame.from_dict(gear_ratio_stats_extended_df, orient='index', columns=[
                                    "fouls", "entry", "racesran", "entry", 60, "entry", 100, "entry", 330, "entry",
                                    660, "entry"])
        gear_ratio_stats_extended_df.set_index(['fouls'], inplace=True)
        return gear_ratio_stats_extended_df


dict_list = data_frames()


def load_dataframes():
    for file_name in os.listdir('cars'):
        if file_name.endswith('.json'):
            selected_car = file_name[:-5]
            file_path = os.path.join('cars', file_name)
            data_frames[selected_car+'_df'] = pd.read_json(file_path, encoding='utf-8')
    globals().update(data_frames)


def clear_all(self):
    self.gear_ratios_df = None
    self.final_ratio_df = None
    self.gear_ratio_stats_df = None
    self.gear_ratio_stats_extended_df = None
    self.gear_ratio_set = None


def clear_gear_ratios_df(self):
    self.gear_ratios_df = None


def clear_final_ratio_df(self):
    self.final_ratio_df = None


def clear_gear_ratio_stats_df(self):
    self.gear_ratio_stats_df = None


def clear_gear_ratio_stats_extended_df(self):
    self.gear_ratio_stats_extended_df = None


def clear_gear_ratio_set(self):
    self.gear_ratio_set = None


class ClearEverything(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.clear_stats_button = QtWidgets.QPushButton(self.mainmenu)
        self.clear_stats_button.setGeometry(QtCore.QRect(620, 350, 75, 23))
        self.clear_stats_button.setObjectName("clear_stats_button")
        self.clear_stats_button.clicked.connect(lambda: clear_stats())

        self.clear_ratios_button = QtWidgets.QPushButton(self.mainmenu)
        self.clear_ratios_button.setGeometry(QtCore.QRect(700, 350, 75, 23))
        self.clear_ratios_button.setObjectName("clear_ratios_button")
        self.clear_ratios_button.clicked.connect(lambda: clear_ratios())
        return print('clear ratios button created')


def clear_stats():
    stats = {"gear_ratio_stats_df", }
    for stat in stats:
        for key in data_frames:
            if stat in key:
                data_frames[key] = pd.DataFrame()


def clear_ratios():
    clear_gear_ratio_set("gear_ratios_df", "final_ratio_df")
    for gear_ratio_set in data_frames:
        for key in data_frames:
            if gear_ratio_set in key:
                data_frames[key] = pd.DataFrame()
