#if (year is not divisible by 4) then (it is a common year)
#else if (year is not divisible by 100) then (it is a leap year)
#else if (year is not divisible by 400) then (it is a common year)
#else (it is a leap year)

#def leap_year(y):
#    if y!/4:
#        print "'y'+"is a common year""
    

#print (leap_year(2016))

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

#http://www.openbookproject.net/thinkcs/python/english2e/ch05.html


def isLeapYear(year):
    if year % 100 != 0:
        if year % 4 == 0:
            return True
    if year % 400 == 0:
        return True
    return False

def isLeapYear(birth_year):
    if birth_year % 100 != 0:
        if birth_year % 4 == 0:
            return True
    if birth_year % 400 == 0:
        return True
    return False

def isLeapYear(today_year):
    if today_year % 100 != 0:
        if today_year % 4 == 0:
            return True
    if today_year % 400 == 0:
        return True
    return False

    
def days_in_last_month(a,b,c):
    today_year=a 
    month=b
    to_day=c
 
    if month==1:
                month_days=31
                days2=to_day-month_days-1
                
    elif month==2:
                                
                        
        if isLeapYear(today_year):
                    month_days=29
        else: month_days=28
        
        days2=to_day-month_days-1

    elif month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                month_days=31
                days2=to_day-month_days-1
             
           
    elif month==4 or month==6 or month==9 or month==11:
                month_days=30
                days2=to_day-month_days-1
    #print (days2)                     
    return (days2)

def days_in_birth_month(a,b,c):
    birth_year=a 
    month=b
    birth_day=c
 
    if month==1:
                month_days=31
                days1=birth_day-1
                
    elif month==2:
                                
                        
        if isLeapYear(birth_year):
                    month_days=29
        else: month_days=28
        
        days1=birth_day-1

    elif month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                month_days=31
                days1=birth_day-1
             
           
    elif month==4 or month==6 or month==9 or month==11:
                month_days=30
                days1=birth_day-1
    #print (days1)                     
    return (days1)



def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    year=year1
    days=0
    month=month1
    birth_day=day1
    
    while year<((year2)+1):
                      
        #print (year)
      
        
        while month<13 :
            
            if month==1:
                month_days=31
                days=days+month_days
                
            elif month==2:
                                
                        
                if isLeapYear(year):
                    month_days=29
                else: month_days=28
                days=days+month_days

            elif month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                month_days=31
                days=days+month_days
             
           
            elif month==4 or month==6 or month==9 or month==11:
                month_days=30
                days=days+month_days
                         
            
            #print (days)
            if year==year2 and month==month2:
                break

            else:
                
                month=month+1
                #print (days)     
        month=1
        year=year+1
    
    return (days+days_in_last_month(year2,month2,day2)-days_in_birth_month(year1,month1,day1))    
        
 
#daysBetweenDates(2013,1,10,2013,1,20)

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            
            print ("Test case passed!")

test()






#http://www.openbookproject.net/thinkcs/python/english2e/ch05.html
