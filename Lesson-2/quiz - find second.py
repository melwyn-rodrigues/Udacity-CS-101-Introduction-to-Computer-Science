#Difficulty level - One Gold Star
# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.
def find_second(source,target):
    first_occurence_position=source.find(target);
    second_occurence_position=source.find(target,first_occurence_position+1);
    return second_occurence_position;
        
    






danton = "De l'audace, encore de l'audace, toujours de l'audace"
print (find_second(danton, 'audace'))
#>>> 25

twister = "she sells seashells by the seashore"
print (find_second(twister,'she'))
#>>> 13
