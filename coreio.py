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

main()





