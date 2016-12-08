###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """

    yr=year
    mth=month
    dy=day
    next_day=dy+1
    if next_day<31:
        print (yr,mth,next_day)
        
    else:
        
        next_day=1
        mth=mth+1
        if mth<13:
            print (yr,mth,next_day)
       
        else:
            mth=1
            yr=yr+1
            print (yr,mth,next_day)

nextDay(2012,12,30)
