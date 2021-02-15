class problem:
    def __init__(self, a ):
        self.array = a

    def find_largest_sequence(self):
        if self.array == [] : return list()
        if len(self.array) == 1 : return self.array
    
        cur_max = set()
        max_so_far = set()
        array = list(set(sorted(self.array)))
        if array.count(array[0]) == len(array) : return [array[0]]
        for i in range(len(array)-1):
            if array[i]+1 == array[i+1] :
                cur_max.add(array[i])
            else:
                if len(cur_max) != 0 : 
                    cur_max.add(array[i])
                
                if len(max_so_far) < len(cur_max):
                        max_so_far = cur_max
                cur_max = set()
        return list(max_so_far)

        

test_cases = { '1' : [1,6,10,4,7,9,5], 
                '2': [],
                '3':[6,6,6,6,6],
                '4': [8],
                '5': [2,9,2,8,9,8,5,7,5,7,9],
                }
answers={ '1' : [4,5,6,7], 
                '2': [],
                '3':[6],
                '4': [8],
                '5': [7,8,9],
                }
for key in test_cases:
    if problem(test_cases[key]).find_largest_sequence() == answers[key]:
        print("{} passed ".format(key))
    else:
        print("{} FAILED".format(int(key)))