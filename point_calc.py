def team_size_pts(size):
    """
    Param: size | type: int
    Return-type: int
    Takes team size as parameter, returns corresponding point value as an int
    """
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

def circ_pts(circ_pct):
    """
    I'm assuming here that the percentage is inputed as a string with a
    percent sign, e.g. traffic_pct = '38%'. Percent sign is stripped then 
    string converted to float. I'll change this if necessary
    
    Param: circ_pct | type: str
    return type: int
    """
    pct = float(circ_pct.strip('%'))
    if pct < 20:
        return 0
    elif  20 <= pct < 30:
        return 5
    elif 30 <= pct < 40:
        return 6
    elif 40 <= pct < 50:
        return 7
    elif 50 <= pct < 60:
        return 8
    elif 60 <= pct < 70:
        return 9
    elif 70 <= pct < 80:
        return 10
    else:
        return 15