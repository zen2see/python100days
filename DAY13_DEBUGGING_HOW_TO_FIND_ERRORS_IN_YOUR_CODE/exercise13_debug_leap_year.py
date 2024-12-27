def is_leap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400 != 0:
                return True
            else:
                return False
        elif year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return False
    else:
        return False
print(is_leap(2020))