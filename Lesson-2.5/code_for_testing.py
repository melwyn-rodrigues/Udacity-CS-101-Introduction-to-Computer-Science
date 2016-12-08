# code for testing code

def no_of_users (a,b):
    total=a+b
    return total




def test():
    test_cases = [((200,100), 300),   # 200, 100 are inputs for procedure 'no_of_users'
                                      # they are called 'arguments' - short form is 'args' 
                                      # 300 is expected output result of the procedure
                                      # they are called 'answer' 
                  ((9,3), 12),
                  ((55000,10000), 65000),
                  ((25,35),60),
                  ((1,4), 5)]
    for (args, answer) in test_cases:  # loop for all test cases - 5 cases in this example
        result = no_of_users(*args)    # output of procedure 'no_of_users' is assigned to variable 'result'
        if result != answer:
            print ("Test with data:", args, "failed")   # test fail - means there is a bug in the code, which needs to be fixed
        else:
            
            print ("Test case passed!")                 # test pass - means code works fine for the test cases

test()
