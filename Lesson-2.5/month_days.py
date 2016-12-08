

def isLeapYear(year):
    if year % 100 != 0:
        if year % 4 == 0:
            return True
    if year % 400 == 0:
        return True
    return False


def month_days(month,year):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        month=31
        return month
                
                
    elif month==2:
        
                                               
        if isLeapYear(year):
            month=29
            return month
        else:
            month=28
            return month
             
    else:
        month=30
        return month
                
print (month_days(4,2012))
