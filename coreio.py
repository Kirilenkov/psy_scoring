import pandas as pd
from bars import bars_medi
import openpyxl as ex
from inputpath import *
from df_filling import core
from processing import processing
from participant_input import participant_data_input

PATH = '/Users/kirill/pr/FFM/psyscoring'
path_setter(PATH)

wb = ex.load_workbook('Scales.xlsx')
scales_names = wb.sheetnames
scales_dict = {str(i): name for name, i in zip(scales_names, range(1, 100))}

# partic_data_df = pd.DataFrame([participant_data_input()])
partic_data_dict = {'full_name': 'УГРЮМОВ ВАСИЛИЙ АЛЕКСЕЕВИЧ', 'dob': '12.12.1987',
                    'filling_date': '22.12.2020', 'visit': '1', 'sex': 'м'}
partic_data_df = pd.DataFrame([partic_data_dict])
mess = 'Выберите опросники по номерам через запятую\n ' \
       'либо введите "в", чтобы выбрать все:'


def scales_choice(message, sc_dict):
    while True:
        print(message)
        for s in sc_dict.items():
            print(s[0], ': ', s[1])
        scl = input()
        output = {}
        if scl == 'в':
            output = sc_dict
            return output
        for ch in scl:
            if ch in sc_dict.keys():
                output[ch] = sc_dict[ch]
        if output.__len__() == 0:
            continue
        else:
            return output


def prepare_df(data_in):
    try:
        if isinstance(data_in, pd.DataFrame):
            df = data_in
        else:
            df = pd.read_excel(data_in, engine='openpyxl', sheet_name='MEDI')
            df = df[['Шкала', 'Значение', 'color']]
    except FileNotFoundError as e:
        print(e)
    else:
        df.drop([0, 1], inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df


scales_chosen = scales_choice(message=mess, sc_dict=scales_dict)

scales_dfs = []

for sc in list(scales_chosen.values()):
    scales_dfs.append((pd.read_excel('Scales.xlsx', engine='openpyxl', sheet_name=sc), sc))

os.chdir('/Users/kirill/Desktop')

file_name = partic_data_df.loc[0, 'full_name']
visit = partic_data_df.loc[0, 'visit']
writer = pd.ExcelWriter(file_name + ' ' + visit + '.xlsx', engine='xlsxwriter')
partic_data_df.to_excel(writer, index=False, sheet_name='Participant')
for i in range(scales_dfs.__len__()):
    method = 'sum'
    scale = scales_dfs[i][1]
    if scale == 'DASS':
        method = 'sum*2'
    elif scale == 'MEDI':
        method = 'mean'
    elif scale == 'TAS-20':
        method = 'common'
    main_data = processing(core(scales_dfs[i][0], scale_name=scales_dfs[i][1]),
                           subscales=True if 'subscales' in scales_dfs[i][0].columns.values else False,
                           mode=method)
    sheet_name = scales_dfs[i][1]
    color_series = main_data['color']
    main_data.at[1, 'Шкала'] = sheet_name
    # main_data.drop(columns=['color'], inplace=True)
    main_data.to_excel(writer, index=False, sheet_name=sheet_name)
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    for j in range(color_series.__len__()):
        color_value = color_series.loc[j]
        if pd.notna(color_value):
            cell_format = workbook.add_format()
            cell_format.set_font_name('Times New Roman')
            cell_format.set_align('left')
            cell_format.set_font_color(color_value)
            worksheet.conditional_format(j + 1, 1, j + 1, 2, {'type':     'text',
                                                              'criteria': 'not containing',
                                                              'value':    'stupid tasks',
                                                              'format':   cell_format})
    if sheet_name == 'MEDI':
        if visit == '2':
            file = file_name + ' ' + '1' + '.xlsx'
            bars_title = file_name + ' 1 и 2'
            df2 = main_data[['Шкала', 'Значение', 'color']]
            bars_medi(visit_1=prepare_df(file), visit_2=prepare_df(df2), title=bars_title)
        if visit == '1':
            bars_title = file_name + ' 1'
            df1 = main_data[['Шкала', 'Значение', 'color']]
            bars_medi(visit_1=prepare_df(df1), title=bars_title)
writer.save()


#     cell_format2 = workbook.add_format()
#     cell_format2.set_font_color('#000000')
#     writer.sheets[sheet_name].set_column(0, 0, None, cell_format2)

# bars(visit_1=df1, visit_2=df2, title=title)
# main_data = pd.read_excel('example.xlsx', sheet_name='MEDI', engine='openpyxl')
# write_log(partic_data_dict, main_data.loc[:, ['Шкала', 'Значение']])'''
