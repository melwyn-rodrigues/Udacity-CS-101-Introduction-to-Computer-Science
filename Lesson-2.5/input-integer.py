#First Test case: Birthday Jan 1 2016 - Today Jan 4 2016 : Age in days = 3 days
#Assume only day input needs to be provided.



birth_day=int(input("Enter Birthday:  "))
print (birth_day)

today_day=int(input("Enter Today_Day:  "))
print (today_day)

print ('Age in Days '  + str(today_day-birth_day)) 
