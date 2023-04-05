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
    for challenger in challenger_df in dataframes.items():
        challenger = pd.concat([challenger_df, gear_ratios_df], axis=1)
        challenger = pd.concat([challenger_df, final_ratio_df], axis=1)
        challenger = pd.concat([challenger_df, gear_ratio_stats_df], axis=1)
        challenger = pd.concat([challenger_df, gear_ratio_stats_extended_df], axis=1)
    return challenger
    challenger_df: pd.read_json(f'cars/challenger.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                                 gear_ratio_stats_df,
                                                                                 gear_ratio_stats_extended_df)

    for charger in charger_df in dataframes.items():
        charger_df = pd.concat([charger_df, gear_ratios_df], axis=1)
        charger_df = pd.concat([charger_df, final_ratio_df], axis=1)
        charger_df = pd.concat([charger_df, gear_ratio_stats_df], axis=1)
        charger_df = pd.concat([charger_df, gear_ratio_stats_extended_df], axis=1)
    return charger
    charger_df: pd.read_json(f'cars/charger.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                             gear_ratio_stats_df,
                                                                             gear_ratio_stats_extended_df)

    for civic in civic_df in dataframes.items():
        civic_df = pd.concat([ccivic_df, gear_ratios_df], axis=1)
        civic_df = pd.concat([civic_df, final_ratio_df], axis=1)
        civic_df = pd.concat([civic_df, gear_ratio_stats_df], axis=1)
        civic_df = pd.concat([civic_df, gear_ratio_stats_extended_df], axis=1)
    return civic
    civic_df : pd.read_json(f'cars/civic.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                             gear_ratio_stats_df,
                                                                             gear_ratio_stats_extended_df)

    for ftype in ftype_df in dataframes.items():
        ftype_df = pd.concat([ftype_df, gear_ratios_df], axis=1)
        ftype_df = pd.concat([ftype_df, final_ratio_df], axis=1)
        ftype_df = pd.concat([ftype_df, gear_ratio_stats_df], axis=1)
        ftype_df = pd.concat([ftype_df, gear_ratio_stats_extended_df], axis=1)
    return ftype
    ftype_df: pd.read_json(f'cars/ftype.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                                gear_ratio_stats_df,
                                                                                gear_ratio_stats_extended_df)

    for funnycar in funnycar_df in dataframes.items():
        funnycar_df = pd.concat([funnycar_df, gear_ratios_df], axis=1)
        funnycar_df = pd.concat([funnycar_df, final_ratio_df], axis=1)
        funnycar_df = pd.concat([funnycar_df, gear_ratio_stats_df], axis=1)
        funnycar_df = pd.concat([funnycar_df, gear_ratio_stats_extended_df], axis=1)
    return funnycar
    funnycar_df: pd.read_json(f'cars/funnycar.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                                gear_ratio_stats_df,
                                                                                gear_ratio_stats_extended_df)

    for lancer in lancer_df in dataframes.items():
        lancer_df = pd.concat([lancer_df, gear_ratios_df], axis=1)
        lancer_df = pd.concat([lancer_df, final_ratio_df], axis=1)
        lancer_df = pd.concat([lancer_df, gear_ratio_stats_df], axis=1)
        lancer_df = pd.concat([lancer_df, gear_ratio_stats_extended_df], axis=1)
    return lancer
    lancer_df: pd.read_json(f'cars/lancer.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                                gear_ratio_stats_df,
                                                                                gear_ratio_stats_extended_df)

    for mopar in mopar_df in dataframes.items():
        mopar_df = pd.concat([mopar_df, gear_ratios_df], axis=1)
        mopar_df = pd.concat([mopar_df, final_ratio_df], axis=1)
        mopar_df = pd.concat([mopar_df, gear_ratio_stats_df], axis=1)
        mopar_df = pd.concat([mopar_df, gear_ratio_stats_extended_df], axis=1)
    return mopar
    mopar_df: pd.read_json(f'cars/mopar.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                                gear_ratio_stats_df,
                                                                                gear_ratio_stats_extended_df)

    for mustang in mustang_df in dataframes.items():
        mustang_df = pd.concat([mustang_df, gear_ratios_df], axis=1)
        mustang_df = pd.concat([mustang_df, final_ratio_df], axis=1)
        mustang_df = pd.concat([mustang_df, gear_ratio_stats_df], axis=1)
        mustang_df = pd.concat([mustang_df, gear_ratio_stats_extended_df], axis=1)
    return mustang
    mustang_df: pd.read_json(f'cars/mustang.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                       gear_ratio_stats_df,
                                                                          gear_ratio_stats_extended_df)

    for ram in ram_df in dataframes.items():
        ram_df = pd.concat([ram_df, gear_ratios_df], axis=1)
        ram_df = pd.concat([ram_df, final_ratio_df], axis=1)
        ram_df = pd.concat([ram_df, gear_ratio_stats_df], axis=1)
        ram_df = pd.concat([ram_df, gear_ratio_stats_extended_df], axis=1)
    return ram
    ram_df: pd.read_json(f'cars/ram.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                        gear_ratio_stats_df,
                                                                            gear_ratio_stats_extended_df)

    for rsx in rsx_df in dataframes.items():
        rsx_df = pd.concat([rsx_df, gear_ratios_df], axis=1)
        rsx_df = pd.concat([rsx_df, final_ratio_df], axis=1)
        rsx_df = pd.concat([rsx_df, gear_ratio_stats_df], axis=1)
        rsx_df = pd.concat([rsx_df, gear_ratio_stats_extended_df], axis=1)
    return rsx
    rsx_df: pd.read_json(f'cars/rsx.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                        gear_ratio_stats_df,
                                                                            gear_ratio_stats_extended_df)

    for rx8 in rx8_df in dataframes.items():
        rx8_df = pd.concat([rx8_df, gear_ratios_df], axis=1)
        rx8_df = pd.concat([rx8_df, final_ratio_df], axis=1)
        rx8_df = pd.concat([rx8_df, gear_ratio_stats_df], axis=1)
        rx8_df = pd.concat([rx8_df, gear_ratio_stats_extended_df], axis=1)
    return rx8
    rx8_df: pd.read_json(f'cars/rx8.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                        gear_ratio_stats_df,
                                                                            gear_ratio_stats_extended_df)

    for skyline in skyline_df in dataframes.items():
        skyline_df = pd.concat([skyline_df, gear_ratios_df], axis=1)
        skyline_df = pd.concat([skyline_df, final_ratio_df], axis=1)
        skyline_df = pd.concat([skyline_df, gear_ratio_stats_df], axis=1)
        skyline_df = pd.concat([skyline_df, gear_ratio_stats_extended_df], axis=1)
    return skyline_df
    skyline_df: pd.read_json(f'cars/skyline.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                          gear_ratio_stats_df,
                                                                            gear_ratio_stats_extended_df)

    for srt4 in srt4_df in dataframes.items():
        srt4_df = pd.concat([srt4_df, gear_ratios_df], axis=1)
        srt4_df = pd.concat([srt4_df, final_ratio_df], axis=1)
        srt4_df = pd.concat([srt4_df, gear_ratio_stats_df], axis=1)
        srt4_df = pd.concat([srt4_df, gear_ratio_stats_extended_df], axis=1)
    return srt4_df
    srt4_df: pd.read_json(f'cars/srt4.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                            gear_ratio_stats_df,
                                                                            gear_ratio_stats_extended_df)

    for subaru in subaru_df in dataframes.items():
        subaru_df = pd.concat([subaru_df, gear_ratios_df], axis=1)
        subaru_df = pd.concat([subaru_df, final_ratio_df], axis=1)
        subaru_df = pd.concat([subaru_df, gear_ratio_stats_df], axis=1)
        subaru_df = pd.concat([subaru_df, gear_ratio_stats_extended_df], axis=1)
    return subaru_df
    subaru_df: pd.read_json(f'cars/subaru.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                            gear_ratio_stats_df,
                                                                            gear_ratio_stats_extended_df)

    for supra in supra_df in dataframes.items():
        supra_df = pd.concat([supra_df, gear_ratios_df], axis=1)
        supra_df = pd.concat([supra_df, final_ratio_df], axis=1)
        supra_df = pd.concat([supra_df, gear_ratio_stats_df], axis=1)
        supra_df = pd.concat([supra_df, gear_ratio_stats_extended_df], axis=1)
    return supra_df
    supra_df: pd.read_json(f'cars/supra.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df,
                                                                            gear_ratio_stats_df,
                                                                            gear_ratio_stats_extended_df)

    for tfd in tfd_df in dataframes.items():
        tfd_df = pd.concat([tfd_df, gear_ratios_df], axis=1)
        tfd_df = pd.concat([tfd_df, final_ratio_df], axis=1)
        tfd_df = pd.concat([tfd_df, gear_ratio_stats_df], axis=1)
        tfd_df = pd.concat([tfd_df, gear_ratio_stats_extended_df], axis=1)
    return tfd_df
    tfd_df: pd.read_json(f'cars/tfd.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df, gear_ratio_stats_df,
                                                                            gear_ratio_stats_extended_df)

    for viper in viper_df in dataframes.items():
        viper_df = pd.concat([viper_df, gear_ratios_df], axis=1)
        viper_df = pd.concat([viper_df, final_ratio_df], axis=1)
        viper_df = pd.concat([viper_df, gear_ratio_stats_df], axis=1)
        viper_df = pd.concat([viper_df, gear_ratio_stats_extended_df], axis=1)
    return viper_df
    viper_df: pd.read_json(f'cars/viper.json').pd.DataFrame.append(gear_ratios_df, final_ratio_df, gear_ratio_stats_df,
                                                                            gear_ratio_stats_extended_df)
