import xlrd
from sys import argv

def open_excel_file(filename):
    '''
    Takes excel workbook file name as argument
    Opens excel workbook
    opens spreadsheets
    returns sheet object(s)
    '''
    workbook = xlrd.open_workbook(filename)
    if workbook.nsheets > 1:
        print("This Excel has too many spreadsheets")
        print("Only 1 spreadsheet can be processed per file")
    else:
        calculate_points(workbook.sheet_by_index(0))
        print(">>>> sheet_object: ", workbook.sheet_by_index(0))

def calculate_points(sheet_object):
    '''
    Takes a sheet object as an an argument.
    Loops through each line of the sheet.
    Extracts team name, wins and OTL and calculates points.
    Note: This assumes we already know which columns we're
    pulling from
    '''
    for i in range(1, sheet_object.nrows):
        points = (sheet_object.row_values(i)[1] * 2) + sheet_object.row_values(i)[3]
        dump_to_text(sheet_object.row_values(i)[0], points)

def dump_to_text(teamname, points):
    results_file.write(f"{teamname}\t{points}\n")

if __name__ == '__main__':
    _, excel_file, text_file = argv
    results_file = open(text_file, "w")
    open_excel_file(excel_file)
    results_file.close()