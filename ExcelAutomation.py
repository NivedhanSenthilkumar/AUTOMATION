

#1-Writing dataframes to Multiple sheets of the same workbook
import pandas as pd
# create  data_frame1 by creating a dictionary
# in which values are stored as list
data_frame1 = pd.DataFrame({'Fruits': ['Appple', 'Banana', 'Mango',
                                       'Dragon Fruit', 'Musk melon', 'grapes'],
                            'Sales in kg': [20, 30, 15, 10, 50, 40]})
# create  data_frame2 by creating a dictionary
# in which values are stored as list
data_frame2 = pd.DataFrame({'Vegetables': ['tomato', 'Onion', 'ladies finger',
                                           'beans', 'bedroot', 'carrot'],
                            'Sales in kg': [200, 310, 115, 110, 55, 45]})
# create  data_frame3 by creating a dictionary
# in which values are stored as list
data_frame3 = pd.DataFrame({'Baked Items': ['Cakes', 'biscuits', 'muffins',
                                            'Rusk', 'puffs', 'cupcakes'],
                            'Sales in kg': [120, 130, 159, 310, 150, 140]})
# create a excel writer object
with pd.ExcelWriter("D:/filename.xlsx") as writer:
    # use to_excel function and specify the sheet_name and index
    # to store the dataframe in specified sheet
    data_frame1.to_excel(writer, sheet_name="Fruits", index=False)
    data_frame2.to_excel(writer, sheet_name="Vegetables", index=False)
    data_frame3.to_excel(writer, sheet_name="Baked Items", index=False)


# 2-Split Excel data in one worksheet into multiple worksheets based on column name.
from xlwings import Workbook, Range, Sheet
import pandas as pd
# Copy this file into the same location as the Excel workbook with the worksheet you wish to split.
# Download the zip of the xlwings Github repo here: https://github.com/ZoomerAnalytics/xlwings and copy the
# xlwings.bas file from the xlwings folder. Import the xlwings.bas file into your Excel workbook by entering ALT+F11
# and then going to File, Import File and clicking on the file.
# Import the Split_Excel_Worksheet.bas file and run by going to the Developer tab on the Excel Ribbon, click Macros,
# and select Split_Excel_Workbooks

# Make sure the data you want split starts in cell A1 and has no empty column headers.
# The worksheet to split should be the first worksheet in the workbook.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Main Script
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def split_worksheets():

    wb = Workbook.caller()

    sheet = Range('temp', 'AA1').value
    column = Range('temp', 'AA2').value

    data = pd.DataFrame(pd.read_excel(sheet, 0, index_col=None, na_values=[0]))
    data.sort(column, axis = 0, inplace = True)

    split = data.groupby(column)
    for i in split.groups:
        Sheet.add()
        Range('A1', index=False).value = split.get_group(i)