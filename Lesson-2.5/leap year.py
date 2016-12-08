#if (year is not divisible by 4) then (it is a common year)
#else if (year is not divisible by 100) then (it is a leap year)
#else if (year is not divisible by 400) then (it is a common year)
#else (it is a leap year)


#print (leap_year(2016))

def isLeapYear(year):
    if year % 100 != 0:       #then it is a leap year
        if year % 4 == 0:     #then it is a leap year 
            return True
    if year % 400 == 0:       #then it is a leap year  
        return True
    return False              #then it is a normal year 
# True represents a leap year
# False represents a normal year

def daysBetweenDates(year):
                if isLeapYear(year):
                    month_days=29
                else: month_days=28

                return (month_days)        

print (daysBetweenDates(2013))



