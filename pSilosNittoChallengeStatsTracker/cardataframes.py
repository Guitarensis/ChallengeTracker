import pandas as pd
from dictionary import gear_ratios_df, gear_ratio_stats_df, gear_ratio_stats_extended_df, final_ratio_df

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
        value = pd.concat([value, gear_ratios_df, final_ratio_df, gear_ratio_stats_df, gear_ratio_stats_extended_df], axis=1)
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

def car_dataframe(dataframes):

    if selected_car == 'challenger':
        return challenger_df
    elif selected_car == 'charger':
        return charger_df
    elif selected_car == 'civic':
        return civic_df
    elif selected_car == 'ftype':
        return ftype_df
    elif selected_car == 'funnycar':
        return funnycar_df
    elif selected_car == 'lancer':
        return lancer_df
    elif selected_car == 'mopar':
        return mopar_df
    elif selected_car == 'mustang':
        return mustang_df
    elif selected_car == 'ram':
        return ram_df
    elif selected_car == 'rsx':
        return rsx_df
    elif selected_car == 'rx8':
        return rx8_df
    elif selected_car == 'skyline':
        return skyline_df
    elif selected_car == 'srt4':
        return srt4_df
    elif selected_car == 'subaru':
        return subaru_df
    elif selected_car == 'supra':
        return supra_df
    elif selected_car == 'tfd':
        return tfd_df
    elif selected_car == 'viper':
        return viper_df
        car_dict = {'gear_ratios_df': gear_ratios_df, 'final_ratio_df': final_ratio_df,
                    'gear_ratio_stats_df': gear_ratio_stats_df,
                    'gear_ratio_stats_extended_df': gear_ratio_stats_extended_df}

        car_df = pd.concat([df for key, df in car_dict.items()], axis=1)
        print(car_df)
    else:
        print("Sorry, we don't have data for that car.")

