import time
test_cases = { '1' : '98202001',
                '2' : '03240000',
                '3' :  '24000024',
                '4' : '110101000'}
answers = { '1' : '00098221',
                '2' : '00000324',
                '3' : '00002424',
                '4' : '000001111'}

answers_last = { '1' : '98221000',
                '2' : '32400000',
                '3' : '24240000',
                '4' : '111100000'}

def arrange_zeroes_last( number:list)->str:
    result = []
    num = [i for i in number if i != '0']
    num_zeros = len(number) - len(num)
    result =  num + ['0']*num_zeros
    return "".join(result)

def arrange_zeroes( number : list ) -> str: #takes longer
    result = []
    num = [i for i in number if i != '0']
    num_zeros = len(number) - len(num)
    result = ['0']*num_zeros + num
    return "".join(result)

def arrange_zeroes_on_itself(number : list) -> str:
    for i, num in enumerate(number):
        if num == '0' :
            number.pop(i)
            number.insert(0,'0')
    return "".join(number)

for key in test_cases.keys():
    start_time = time.time()
    res = arrange_zeroes_last(list(test_cases[key]))
    #print("CASE: ",test_cases[key],", Result : ",res ,', Solution: ',answers_last[key])
    if res == answers_last[key]:
        print("{} passed".format(key))
      #  print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("{} FAILED".format(key))