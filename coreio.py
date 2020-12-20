import pandas as pd
# import main_objects
import openpyxl as ex
from inputpath import *

PATH = '/Users/kirill/pr/FFM/psyscoring'
path_setter(PATH)

sheets_amount = len(ex.load_workbook('Scales.xlsx').worksheets)
scales_df = []

for i in range(sheets_amount):
    scales_df.append(pd.read_excel('Scales.xlsx', engine='openpyxl', sheet_name=i))

print(scales_df)




