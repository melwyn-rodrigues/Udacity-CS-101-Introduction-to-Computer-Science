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




def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    year=year1
    month=month1
    days=1-day1  # this removes the days in the first month starting from 1st till the day1
                 #(excluding the day1 - that's why you have the 1 before the substraction)
    
    while year<((year2)+1):
                   
        #print (year) 
       
        while month<13 :             # this condition checks whether the current year has ended with 12 months
                                     # and if it has , control jumps to line 76 where the month is initialized to Jan (month=1)

                                     # and the year is initialized to the next year (year=year+1)
            
            if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                month_days=31
                days=days+month_days
                
            elif month==2:
                                               
                if isLeapYear(year):
                    month_days=29
                else: month_days=28
                days=days+month_days
             
            else:           
                month_days=30        # This condition refers to months 4,6,9,11
                days=days+month_days
                         
            #print (days)
            if year==year2 and month==month2:  # condition to check, after each 'while month' cycle, whether loop has reached the
                                               # end of the process which is the last month and year (year2 , month2)
                days=days+(day2-month_days-1) # (day2-month_days-1)removes the remaining days (after day2) in the last month 
                                            #(including the day2 - that's why you have the -1 in the calculation)
                #break
                return (days)         # Final result. Value returned to procedure def test()- line 89
            else:
                
                month=month+1        # end of 'while month' loop. Control goes back to start of loop (line 46)
                #print (days)     
        month=1
        year=year+1                   # end of 'while year' loop. Control goes back to start of loop (line 42) 
    

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
# Version 1 of my code had 100 lines.
#changes done in version2
#1.all months which are 31 are clubbed together.
#2.all months which are 30 moved to else, thereby removing need for elif
# the above three improvements resulted in reducing 3 code lines
#3. procedure isLeapYear reduced from three to only one.
#the above improvement resulted in reducing 14 code lines
#4. Eliminated procedure days_in_birth_month by adding one new line 'days=1-day1'
# Pt. 4 helped to reduce a further 20 lines
#pt.5. Eliminated procedure days_in_last_month by adding one new line 'days=days+day2-month_days-1
# pt. 5 helped to reduce a further 18 lines.
# Final : my program has 45 lines . Lisa Dong/Dave's program has 55 lines. It appears that I can write a efficient program.
# Compared to my version 1 of 100 code lines, I managed more than 50% efficiency by reducing 55 code lines (total
# code lines 45) in version 2 by learning tricks from Dave/Lisa Dong's code.


#http://www.openbookproject.net/thinkcs/python/english2e/ch05.html
