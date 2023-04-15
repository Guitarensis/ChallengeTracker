import pandas as pd
from dictionary import gear_ratios_df, gear_ratio_stats_df, gear_ratio_stats_extended_df, final_ratio_df
import processnitto


dataframes = {
    'challenger_df': pd.read_json(f'cars/challenger.json'),
    'charger_df': pd.read_json(f'cars/charger.json'),
    'civic_df': pd.read_json(f'cars/civic.json'),
    'ftype_df': pd.read_json(f'cars/ftype.json'),
    'funnycar_df': pd.read_json(f'cars/funnycar.json'),
    'lancer_df': pd.read_json(f'cars/lancer.json'),
    'mopar_df': pd.read_json(f'cars/mopar.json'),
    'mustang_df': pd.read_json(f'cars/mustang.json'),
    'ram_df': pd.read_json(f'cars/ram.json'),
    'rsx_df': pd.read_json(f'cars/rsx.json'),
    'rx8_df': pd.read_json(f'cars/rx8.json'),
    'skyline_df': pd.read_json(f'cars/skyline.json'),
    'srt4_df': pd.read_json(f'cars/srt4.json'),
    'subaru_df': pd.read_json(f'cars/subaru.json'),
    'supra_df': pd.read_json(f'cars/supra.json'),
    'tfd_df': pd.read_json(f'cars/tfd.json'),
    'viper_df': pd.read_json(f'cars/viper.json')
}

for key, value in dataframes.items():
    if key.endswith('_df'):
        value = pd.concat([value, gear_ratios_df, final_ratio_df, gear_ratio_stats_df, gear_ratio_stats_extended_df],
                          axis=1)
        dataframes[key] = value

challenger_df = dataframes['challenger_df']
charger_df = dataframes['charger_df']
civic_df = dataframes['civic_df']
ftype_df = dataframes['ftype_df']
funnycar_df = dataframes['funnycar_df']
lancer_df = dataframes['lancer_df']
mopar_df = dataframes['mopar_df']
mustang_df = dataframes['mustang_df']
ram_df = dataframes['ram_df']
rsx_df = dataframes['rsx_df']
rx8_df = dataframes['rx8_df']
skyline_df = dataframes['skyline_df']
srt4_df = dataframes['srt4_df']
subaru_df = dataframes['subaru_df']
supra_df = dataframes['supra_df']
tfd_df = dataframes['tfd_df']
viper_df = dataframes['viper_df']


def car_dataframe(selected_car):
    if selected_car in dataframes:
        df = dataframes[selected_car]
        return pd.concat([df, gear_ratios_df, final_ratio_df, gear_ratio_stats_df, gear_ratio_stats_extended_df],
                         axis=1)
    else:
        print("Sorry, we don't have data for that car.")


selected_car = processnitto.get_car()
df = car_dataframe(selected_car)
