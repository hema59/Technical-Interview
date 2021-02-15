test_cases = { '1' :[1,2,1,2,4,3,2,3,2,1] ,
                '2' :[3,3,3,3,4,3,3,1,1,1],
                '3' :[],
                '4': [1],
                '5':[5,5,5,5] }
answers =  { '1' : [1,4],
                '2' :[1,4],
                '3' :[],
                '4' : [1],
                '5' :[]}
def find_odd_count( array ):
    if len(array) == 0 : return []
    if len(array) == 1 : return array
    count = dict()
    for i in array:
        count[i] = array.count(i)
    result = set( [h for h in count.keys() if count[h]%2 != 0] )
    return list(result)

for key in test_cases.keys():
    result = find_odd_count(test_cases[key])
    if result == answers[key]:
        print("{} PASSED".format(key))            
    else:
        print("{} FAILED".format(key))            