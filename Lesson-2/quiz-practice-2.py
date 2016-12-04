#assume test is a procedure takes a number as its input and outputs a Boolean
#original
def test(a):
    return True

def proc(a,b):
    if test(a):
        return b
    return a

print (proc(2,3))

#Result: outcome is 3
#option 1
def test(x):
    return True

def proc1(x,y):
    if test(x):
        return y
    return x

print (proc1(2,3))

#Result: outcome of option 1(is 3) is same as the outcome of 'original'( is 3)

#option 2
def test(b):
    return ?

def proc2(a,b):
    if test(b):
        return a
    else:
        return b

print (proc2(2,3))

#Result: This option evaluates test(b), which is different from the original. Therefore the outcome of option 2 cannot be compared to the outcome of 'original'(is 3)

#option 3
def test(a):
    return True

def proc3(a,b):
    result=a
    if test(a):
        result=b
    return result

print (proc3(2,3))

#Result: outcome of option 3(is 3) is same as the outcome of 'original'(is 3)


#option 4
def test(a):
    return False

def proc4(a,b):
        if test(a):
            b='udacity'
        else:
            return b
        return a
        
print (proc4(2,3))

#Result: outcome of option 4(is 3) is same as the outcome of 'original'(is 3)












