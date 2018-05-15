import xlrd
import csv

"""
This is a utility script for Her Campus staff. 
It is designed to calulate the monthly points for team size,
social circulation, and traffic circulation. 
After calculating points, the script will write the totals
to a .csv file
"""


def team_size_pts(size):
    """
    Param: size | type: int
    Return-type: int
    Takes team size as parameter as extracted from spreadsheet, 
    returns corresponding point value as an int
    """
    try:
        if size < 10:
            return 0
        elif 10 <= size < 15:
            return 3
        elif 15 <= size < 20:
            return 6
        elif 20 <= size < 30:
            return 7
        elif 30 <= size < 50:
            return 8
        else:
            return 10
    except TypeError:
        return 0

def circ_pts(circ_pct):
    """
    Param: circ_pct | type: float
    return type: int
    Given the circulation percentage as a float,
    This function returns the corresponding number of points as an int
    """
    try:
        if circ_pct < 0.2:
            return 0
        elif  0.2 <= circ_pct < 0.3:
            return 5
        elif 0.3 <= circ_pct < 0.4:
            return 6
        elif 0.4 <= circ_pct < 0.5:
            return 7
        elif 0.5 <= circ_pct < 0.6:
            return 8
        elif 0.6 <= circ_pct < 0.7:
            return 9
        elif 0.7 <= circ_pct < 0.8:
            return 10
        else:
            return 15
    except TypeError:
        return 0


if __name__ == '__main__':
    # opens mccm.xlsx workbook
    workbook = xlrd.open_workbook('mccm.xlsx')
    # gets the sheet object for the 'Campuses' sheet
    campuses = workbook.sheet_by_index(3)

    # opens/truncates points.csv file
    with open('points.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter='\t', lineterminator='\n')
        csv_writer.writerow(["Chapter", "Team Points", 
                             "Social Circ", "Traffic Circ", "Total Points"])
    
        for i in range(1, campuses.nrows):
            # checks if first cell in each column is blank
            if not campuses.cell_value(i, 0) == '':
                chapter = campuses.row_values(i)[0]
                team = team_size_pts(campuses.row_values(i)[18])
                social_circ = circ_pts(campuses.row_values(i)[64])
                traffic_circ = circ_pts(campuses.row_values(i)[68])
                total = team + social_circ + traffic_circ
                csv_writer.writerow([chapter, team, social_circ, traffic_circ, total])
            else:
                break