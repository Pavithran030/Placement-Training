def is_leap(leap):
    leap=False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return leap
        else:
            return True
    else:
        return leap


