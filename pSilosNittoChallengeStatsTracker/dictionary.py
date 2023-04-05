import pandas as pd
from PyQt5 import QtCore, QtWidgets
import os


dataframes = {
    'challenger_df': pd.DataFrame(...),
    'charger_df': pd.DataFrame(...),
    'civic_df': pd.DataFrame(...),
    'ftype_df': pd.DataFrame(...),
    'funnycar_df': pd.DataFrame(...),
    'lancer_df': pd.DataFrame(...),
    'mopar_df': pd.DataFrame(...),
    'mustang_df': pd.DataFrame(...),
    'ram_df': pd.DataFrame(...),
    'rsx_df': pd.DataFrame(...),
    'rx8_df': pd.DataFrame(...),
    'skyline_df': pd.DataFrame(...),
    'srt4_df': pd.DataFrame(...),
    'subaru_df': pd.DataFrame(...),
    'supra_df': pd.DataFrame(...),
    'tfd_df': pd.DataFrame(...),
    'viper_df': pd.DataFrame(...),
    'gear_ratios_df': pd.DataFrame({...}),
    'final_ratio_df': pd.DataFrame({...}),
    'gear_ratio_stats_df': pd.DataFrame({...}),
    'gear_ratio_stats_extended_df': pd.DataFrame({...})
}


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


def dataframes():
    try:
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

        gear_ratios_df = pd.DataFrame.from_dict(gear_ratios, orient='index', columns=['gear1', 0, 'gear2', 0, 'gear3',
                                                                                      0, 'gear4', 0, 'gear5', 0,
                                                                                      'gear6', 0])
        gear_ratios_df.set_index('gear1', inplace=True)
        return gear_ratios_df
    except Exception:
        raise ValueError(f'Error: ', f'Erro creating {gear_ratios_df} dataframe')

        try:
            final_ratio = {"gear_ratio_set_1": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_2": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_3": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_4": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_5": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_6": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_7": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_8": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_9": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_10": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_11": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_12": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_13": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_14": ["final", 0, "expectedet", 0],
                           "gear_ratio_set_15": ["final", 0, "expectedet", 0]}

            final_ratio_df = pd.DataFrame. from_dict(final_ratio, orient='columns').transpose()
            final_ratio_df.columns = ['final', "entry", 'expectedet', "entry"]
            final_ratio_df.set_index(['final', 'expectedet'], inplace=True)
            return final_ratio_df
        except Exception:
            raise ValueError(f'Error: ', f'Erro creating {final_ratio_df} dataframe')

    try:
        gear_ratio_stats = {"gear_ratio_set_1": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_2": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_3": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_4": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_5": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_6": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_7": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_8": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_9": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_10": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_11": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_12": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_13": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_14": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0],
                            "gear_ratio_set_15": ["rt", 0, "et", 0, "mph", 0, "rtdiff", 0, "etdiff", 0, "mphdiff", 0]}

        gear_ratio_stats_df = pd.DataFrame.from_dict(gear_ratio_stats, orient='columns').transpose()
        gear_ratio_stats_df.columns = ['rt', "entry",  'et', "entry", 'mph', "entry",  'rtdiff', "entry",
                                       'etdiff', "entry",  'mphdiff', "entry"]
        gear_ratio_stats_df.set_index(['rt', 'et', 'mph', 'rtdiff', 'etdiff', 'mphdiff'], inplace=True)
        return gear_ratio_stats_df
    except Exception:
        raise ValueError(f'Error: ', f'Erro creating {gear_ratio_stats_df} dataframe')

    try:
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

        gear_ratio_stats_extended_df() = pd.DataFrame.from_dict(gear_ratio_stats_extended, orient='columns').transpose()
        gear_ratio_stats_extended_df.columns = ['fouls', "entry",  'racesran', "entry"]
        gear_ratio_stats_extended_df.set_index(['fouls', 'racesran'], inplace=True)
        return gear_ratio_stats_extended_df
    except Exception:
        raise ValueError(f'Error: ', f'Erro creating {gear_ratio_stats_extended_df} dataframe')

    challenger_df: pd.read_json(f'cars/challenger.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                             gear_ratio_stats_df,
                                                                             gear_ratio_stats_extended_df)
    charger_df: pd.read_json(f'cars/charger.json').pd.DataFrame.append(gear_ratio_set_df, final_ratio_df,
                                                                       gear_ratio_stats_df, gear_ratio_stats_extended_df
                                                                       )
    civic_df: pd.read_json(f'cars/civic.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df, gear_ratio_stats_df,
                                                                   gear_ratio_stats_extended_df)
    ftype_df: pd.read_json(f'cars / ftype.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                     gear_ratio_stats_df, gear_ratio_stats_extended_df)
    funnycar_df: pd.read_json(f'cars/funnycar.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df,
                                                                         gear_ratio_stats_df,
                                                                         gear_ratio_stats_extended_df)
    lancer_df: pd.read_json(f'cars/lancer.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df, gear_ratio_stats_df,
                                                                  gear_ratio_stats_extended_df)
    mopar_df: pd.read_json(f'cars/mopar.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df, gear_ratio_stats_df,
                                                                   gear_ratio_stats_extended_df)
    mustang_df: pd.read_json(f'cars/mustang.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df,
                                                                       gear_ratio_stats_df,
                                                                       gear_ratio_stats_extended_df)
    ram_df: pd.read_json(f'cars/ram.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df, gear_ratio_stats_df,
                                                               gear_ratio_stats_extended_df)
    rsx_df: pd.read_json(f'cars/rsx.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df, gear_ratio_stats_df,
                                                               gear_ratio_stats_extended_df)
    rx8_df: pd.read_json(f'cars/rx8.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df, gear_ratio_stats_df,
                                                               gear_ratio_stats_extended_df)
    skyline_df: pd.read_json(f'cars/skyline.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df,
                                                                       gear_ratio_stats_df,
                                                                       gear_ratio_stats_extended_df)
    srt4_df: pd.read_json(f'cars/srt4.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df, gear_ratio_stats_df,
                                                                 gear_ratio_stats_extended_df)
    subaru_df: pd.read_json(f'cars/subaru.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df, gear_ratio_stats_df,
                                                                     gear_ratio_stats_extended_df)
    supra_df: pd.read_json(f'cars/supra.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df, gear_ratio_stats_df,
                                                                   gear_ratio_stats_extended_df)
    tfd_df: pd.read_json(f'cars/tfd.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df, gear_ratio_stats_df,
                                                               gear_ratio_stats_extended_df)
    viper_df: pd.read_json(f'cars/viper.json').pd.DataFrame.append(gear_ratio_df, final_ratio_df, gear_ratio_stats_df,
                                                                   gear_ratio_stats_extended_df)

    # Print the DataFrames
    print(gear_ratios_df)
    print(final_ratio_df)
    print(gear_ratio_stats_df)
    print(gear_ratio_stats_extended_df)


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
    global dataframes
    stats = {"gear_ratio_stats_df", }
    for stat in stats:
        for key in dataframes:
            if stat in key:
                dataframes[key] = pd.DataFrame()


def clear_ratios():
    global dataframes
    ratios = {"gear_ratios_df", "gear_ratio_stats_df", "gear_ratio_stats_extended_df", "final_ratio_df"}
    for ratio in ratios:
        for key in dataframes:
            if ratio in key:
                dataframes[key] = pd.DataFrame()


dict_list = dataframes()


def load_dataframes():
    car_dataframes = {}
    for file_name in os.listdir('cars'):
        if file_name.endswith('.json'):
            selected_car = file_name[:-5]
            file_path = os.path.join('cars', file_name)
            dataframes[selected_car+'_df'] = pd.read_json(file_path)
    globals().update(dataframes)
