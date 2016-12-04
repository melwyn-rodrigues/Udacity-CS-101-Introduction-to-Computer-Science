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
    if a==big and b>=c:
        return b
    if a==big and b<c:
        return c

    if b==big and a>=c:
        return a
    if b==big and a<c:
        return c

    if c==big and a>=b:
        return a
    if c==big and a<b:
        return b

print(median(5,2,2))
#>>> 2

#print(median(9,3,6))
#>>> 6

#print(median(7,8,7))
#>>> 7
