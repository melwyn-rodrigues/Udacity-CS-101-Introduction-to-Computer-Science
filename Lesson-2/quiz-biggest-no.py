# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def first(a,b):
    if a>b:
        return a
    else:
        return b
    



def biggest(a,b,c):
    first_output=first(a,b)
    if first_output>c:
        return first_output
    else:
        return c
    

#print (biggest(3, 6, 9))
#>>> 9

#print (biggest(6, 9, 3))
#>>> 9

#print (biggest(9, 3, 6))
#>>> 9

#print (biggest(3, 3, 9))
#>>> 9

#print (biggest(9, 3, 9))
#>>> 9

print (biggest(8, 7, 9))
#>>> 9
