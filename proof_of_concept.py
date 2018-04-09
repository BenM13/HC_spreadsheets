import xlrd
import csv
from sys import argv

'''
This is a proof-of-concept script to help with the final product
The script was written for a specific Excel file in which 
we already what type of data to expect in each of the columns
(in this case, the 2018 NHL standings)
In this example, it will take a spreadsheet with each NHL teams' 2018 win-loss record
and will calculate the total points
(In hockey 2 points for a win, 1 point for an overtime/shootout loss)
'''

def calculate_points(sheet_object):
    row_vals = []
    for i in range(1, sheet_object.nrows):
        points = (sheet_object.row_values(i)[1] * 2) + sheet_object.row_values(i)[3]
        row_vals.append([sheet_object.row_values(i)[0], int(points)])
    dump_to_csv(row_vals)

def dump_to_csv(vals):
    with open('results.csv', "w") as file:
        writer = csv.writer(file, delimiter='\t', lineterminator='\n')
        writer.writerows(vals)

if __name__ == '__main__':
    '''
    Takes Excel file name and sheet name as command line arguments
    Checks if given sheet name exists in file. 
    If the sheet doesn't exist, an error messager is displayed. 
    '''
    _, excel_file, sheet_name = argv
    workbook = xlrd.open_workbook(excel_file)
    if sheet_name not in workbook.sheet_names():
        print(f"There is no sheet named {sheet_name} in this excel file")
    else:
        calculate_points(workbook.sheet_by_name(sheet_name))