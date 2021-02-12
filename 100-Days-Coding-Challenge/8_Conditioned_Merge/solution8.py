
def solution( a1, a2):
    result = sorted(set(a1+a2))
    return [i for i in result if i >= 0 ]
     

test_cases = { '1' : [[2,13,4,6],[8,-5,4]],
                '2': [[],[2,3]],
                '3' :[[9,3,5],[5]],
                '4' :[[-1,3,-7,2, 3,-2,1],[-2,10,0]] }
merge_answer = { '1' : [2, 4, 6, 8, 13], '2': [2, 3],'3':[3, 5, 9],'4':[0, 1, 2, 3, 10]}

print("Conditioned Merge")
for key in test_cases.keys():
    if merge_answer[key] == solution(test_cases[key][0], test_cases[key][1]):
        print("Test case {} passed".format(key))

#assuming that the conditions hold for this extra bit
def merge(a1,a2):
    a1 = set([i for i in a1 if i >=0 ])
    a2 = sorted([i for i in a2 if i >=0 ])
    while len(a2)>0:
        t = a2.pop()
        if t not in a1:
            a1.add(t)
    a1 = list(a1)
    a1.sort()
    return a1

print("Merging without third array")
for key in test_cases.keys():
    if merge_answer[key] == merge(test_cases[key][0], test_cases[key][1]):
        print("Test case {} passed".format(key))


