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
    
    Param: circ_pct | type: float
    return type: int
    """
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