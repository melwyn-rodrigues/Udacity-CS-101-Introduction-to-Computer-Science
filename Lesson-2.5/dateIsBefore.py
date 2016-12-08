def dateIsBefore(year1,month1,day1,year2,month2,day2):
    if year2>year1:
        return True
    if year2==year1:
        if month2>month1:
            return True
        if month2==month1:
            if day2>day1:
                return True
    return False

    

print (dateIsBefore(2016,12,7,2016,12,5))
