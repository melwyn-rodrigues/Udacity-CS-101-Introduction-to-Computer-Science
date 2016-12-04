# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    big=biggest(a,b,c)
    if big==a:
        return bigger(b,c)         
        
    if big==b:
        return bigger(a,c)

    if big==c:
        return bigger(a,b)
    

print(median(2,1,5))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,9))
#>>> 7
