test_cases = {'1': [0, -1, 3, 100, -70, -5],
            '2' : [1, 3, 5, 2, 8, 0, -1, 3]}
answers = {'1':300, '2':720}

#assuming without repetition
def find_highest_prod( array):
    if len(array) == 0 : return []
    if len(array) <= n : return array
    array = sorted(array)
    cur_max = max_so_far = 1
    for item in array:
        cur_max = max( cur_max, item * cur_max )
        max_so_far = max( max_so_far, cur_max)
    print(max_so_far)
    return max_so_far

n=3
for key in test_cases:
    if find_highest_prod(test_cases[key])== answers[key]:
        print("{} Passed".format(key))
    else:
        print("{} FAILED".format(key))