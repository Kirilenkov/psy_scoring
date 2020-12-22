import pandas as pd
# import main_objects
import openpyxl as ex
from inputpath import *
from participant_input import main

PATH = '/Users/kirill/pr/FFM/psyscoring'
path_setter(PATH)

wb = ex.load_workbook('Scales.xlsx')
scales_names = wb.sheetnames
sheets_amount = len(scales_names)
scales_df = []

for i in range(sheets_amount):
    scales_df.append(pd.read_excel('Scales.xlsx', engine='openpyxl', sheet_name=i))

scales_names = wb.sheetnames

# partic_data_dict = main()

partic_data_dict = {'full_name': 'ВАСИЛЬЕВ ВАСИЛИЙ АЛЕКСЕЕВИЧ', 'dob': '12.12.1987',
                    'filling_date': '22.12.2020', 'visit': '1', 'sex': 'м'}


def scales_choice():
    while True:
        print('Выберите опросники по номерам через запятую\n'
              'либо введите "в", чтобы выбрать все:')
        counter = 0
        for s, i in zip(scales_names, range(100)):
            print(str(i + 1) + '. {}'.format(s))
            counter += i
        output = ''
        for n in range(counter):
            output += str(counter + 1) + ','
        sc = input()
        if sc == 'в':
            return output[:-1]
        # Требуется проверка ввода и обработка исключений
        else:
            return sc


scales_choice()











