def find_missing( array ):
    if len(array) <= 1 : return False
    for i in range(array[len(array)-1]):
        if array[i+1] != array[i]+1:
            return array[i]+1
    return False

def first_repeating( array ):
    if len(array) <= 1: return False
    for i in array:
        if array.count(i) != 1:
            return i
    return False

test_cases1 = { '1' :[2,3,4,5,6,8,9,10,12],
                '2' :[2,3,4,5,6,7,8,9,10,12],
                '3' :[],
                '4' : [3,3,3,3,3],
                '5' :[3,4,5,7,7]}
test_cases2 = { '1' :[2,3,4,5,6,8,9,10,12],
                '2' :[2,3,12,4,5,6,7,8,9,10,12],
                '3' :[],
                '4' : [3,3,3,3,3],
                '5' :[3,4,5,7,7]}
answers1 = { '1' :7,
            '2' :11,
            '3' : False,
            '4' : 4, '5': 6}
answers2 = { '1' :False,
            '2' :12,
            '3' :False,
            '4' :3,'5': 7}
print("Finding first missing number")
for key in test_cases1.keys() :
    if find_missing(test_cases1[key] ) == answers1[key] :     
        print("{} PASSED".format(key))
    else:
        print("{} FAILED".format(key))

print("Finding first repeating number")
for key in test_cases2.keys() :
    if first_repeating(test_cases2[key] ) == answers2[key] :     
        print("{} PASSED".format(key))
    else:
        print("{} FAILED".format(key))