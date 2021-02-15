test_cases = { '1' :12321,
                '2': 18822,
                '3': -900,
                '4': 149072,
                '5' : 444}
answers = { '1' :12321,
                '2': 22881,
                '3': -9,
                '4':270941,
                '5':444 }

def get_digits( number ):
    array =  []
    t = number
    while t > 0:
        array.append(str(t%10))
        t = t//10
    return array

def reverse_me( number ):
    sign = -1 if number < 0 else 1
    if number >= 0 and number < 10: return  sign*number
    number = get_digits(abs(number))
    result = int("".join(number))
    return sign*result


for key in test_cases.keys():
    if reverse_me(test_cases[key]) == answers[key]:
            print("{} passed".format(key))
    else:
            print("{} FAILED".format(key))
