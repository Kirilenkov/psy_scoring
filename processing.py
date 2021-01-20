import pandas as pd


def inverter(min, max, val):
    seq = [i for i in range(min, max + 1)]
    i = seq.index(val)
    seq.reverse()
    return seq[i]


def generator(val):
    while True:
        val += 1
        yield val


def processing(df, mode, subscales=False):
    weight = 1
    if mode == 'sum*2':
        weight = 2
    scales = dict()
    df_len = df.__len__()
    df_output = pd.DataFrame()
    min_range = int(df.loc[0, 'range_min'])
    max_range = int(df.loc[0, 'range_max'])
    for i in range(df_len):
        if int(df.loc[i, 'score']) > 0:
            df.loc[i, 'ans_filtered'] = inverter(min=min_range, max=max_range, val=int(df.loc[i, 'answer']))
        else:
            df.loc[i, 'ans_filtered'] = int(df.loc[i, 'answer'])

    counter = 0
    for i in range(df_len):
        counter += int(df.loc[i, 'ans_filtered'])
    # df_output.loc[0, 'Общая сумма'] = counter
    scales['Общая сумма'] = counter

    if subscales:
        for i in range(df_len):
            name = df.loc[i, 'subscales']
            if name in scales:
                scales[name] = scales[name] + int(df.loc[i, 'ans_filtered'])*weight
            else:
                scales[name] = int(df.loc[i, 'ans_filtered'])*weight
    for place_holder in ['Шкала', 'Значение', 'Градация']:
        df_output[place_holder] = ''
    gen = generator(0)
    for sc_name in scales.keys():
        index = next(gen)
        value = scales[sc_name]
        df_output.loc[0, sc_name] = value
        df_output.loc[index, 'Шкала'] = sc_name
        df_output.loc[index, 'Значение'] = value

    for i in range(df_len):
        verbose_report_quest = str(df.loc[i, 'seq']) + ' ' + df.loc[i, 'quest']
        df_output.loc[0, verbose_report_quest] = df.loc[i, 'answer']
    print(df_output)
    return df_output
