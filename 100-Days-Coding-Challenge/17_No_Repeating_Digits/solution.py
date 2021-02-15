test_cases = { '1' : { 'upper_bound' :100 , 'lower_bound' : 25} ,
                '2' :{ 'upper_bound' : 130 , 'lower_bound' : 100},
                '3' :{ 'upper_bound' : 1023 , 'lower_bound' : 999}
                }
answers = { '1' :[33,44,55,66,77,88,99] ,
                '2' :[101,110,111,112,113,114,115,116,117,118,119,122,121],
                '3' : [999,1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,
                        1014,1015,1016,1017,1018,1019,1020,1021,1022] #should prnt only 1023 😄
                }

def get_digits( number ):
    array =  []
    t = number
    while t > 0:
        array.append(str(t%10))
        t = t//10
    return array

def has_repeating(array):
    for i in array:
        if array.count(i) != 1:
            return True
    return False

def get_no_repeating_digits( bounds) :
    upper = bounds['upper_bound']
    lower = bounds['lower_bound']

    result = []
    for i in range(lower, upper+1):
        stack = get_digits(i)
        if has_repeating(stack) == False:
            result.append(i)
    return result

for key in test_cases.keys():
    check = False
    result = get_no_repeating_digits(test_cases[key])
    for i in result:
        if i in answers[key]:
            break
        else:
            check = True
    if check == True:
        print("{} PASSED".format(key))
    else:
        print("{} FAILED".format(key))