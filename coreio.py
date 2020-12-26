import pandas as pd
# import main_objects
import openpyxl as ex
from inputpath import *
from participant_input import main

PATH = '/Users/kirill/pr/FFM/psyscoring'
path_setter(PATH)

wb = ex.load_workbook('Scales.xlsx')
scales_names = wb.sheetnames

scales_dict = {str(i): name for name, i in zip(scales_names, range(1, 100))}

# partic_data_dict = main()

partic_data_dict = {'full_name': 'ВАСИЛЬЕВ ВАСИЛИЙ АЛЕКСЕЕВИЧ', 'dob': '12.12.1987',
                    'filling_date': '22.12.2020', 'visit': '1', 'sex': 'м'}


def scales_choice(message, sc_dict):
    while True:
        # sequence = []
        print(message)
        for s in sc_dict.items():
            print(s[0], ': ', s[1])
        sc = input()
        output = {}
        if sc == 'в':
            output = sc_dict
            return output
        for ch in sc:
            if ch in sc_dict.keys():
                output[ch] = sc_dict[ch]
                # sequence.append(ch)
        if output.__len__() == 0:
            continue
        else:
            return output


mess = 'Выберите опросники по номерам через запятую\n ' \
       'либо введите "в", чтобы выбрать все:'
scales_chosen = scales_choice(message=mess, sc_dict=scales_dict)

scales_df = []

for sc in list(scales_chosen.values()):
    scales_df.append(pd.read_excel('Scales.xlsx', engine='openpyxl', sheet_name=sc))
