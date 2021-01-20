import pandas as pd
# import main_objects
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
partic_data_dict = {'full_name': 'ВАСИЛЬЕВ ВАСИЛИЙ АЛЕКСЕЕВИЧ', 'dob': '12.12.1987',
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


scales_chosen = scales_choice(message=mess, sc_dict=scales_dict)

scales_dfs = []

for sc in list(scales_chosen.values()):
    scales_dfs.append((pd.read_excel('Scales.xlsx', engine='openpyxl', sheet_name=sc), sc))

os.chdir('/Users/kirill/Desktop')
writer = pd.ExcelWriter(partic_data_df.loc[0, 'full_name'] + '.xlsx')
partic_data_df.to_excel(writer, index=False, sheet_name='Participant')
for i in range(scales_dfs.__len__()):
    method = 'sum'
    if scales_dfs[i][1] == 'DASS':
        method = 'sum*2'
    main_data = processing(core(scales_dfs[i][0], scale_name=scales_dfs[i][1]),
                           subscales=True if 'subscales' in scales_dfs[i][0].columns.values else False,
                           mode=method)
    main_data.to_excel(writer, index=False, sheet_name=scales_dfs[i][1])
writer.save()
