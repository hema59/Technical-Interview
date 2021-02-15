def find_intersection( bundle ):
    a1 = bundle['A']
    a2 = bundle['B']
    if len(a1) == 0 or len(a2) == 0: return []
    result = []
    for i in a1:
        if i in a2:
            result.append(i)
            a2.remove(i)
    return result 

test_cases = { '1' : { 'A' : [1,2,3,4,5,6,7],
                        'B':[0,9,10,4,5] },
                '2' : { 'A' :[1,2,3,4,5,6,6,6,7],
                        'B' :[0,6,9,10,6,4,5] },
                '3' : { 'A' : [],
                        'B' : [2,3,4]},
                '4' : { 'A' :[],
                        'B' : [] },
                '5' : { 'A' :[1,2,3],
                        'B' : [4,5,6,7] } }
answers = { '1' : [4,5],
            '2' : [4,5,6,6],
            '3' :[],
            '4' :[],
            '5' :[]}
for key in test_cases.keys():
    result = find_intersection( test_cases[key] )
    if result == answers[key]:
        print("{} PASSED".format(key))
    else:
        print("{} FAILED".format(key))
