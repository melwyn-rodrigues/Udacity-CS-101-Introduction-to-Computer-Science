# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    total=n
    while n>1:
        total=total*(n-1)
        n=n-1
    return total


print (factorial(4))
#>>> 24
print (factorial(5))
#>>> 120
print (factorial(6))
#>>> 720
