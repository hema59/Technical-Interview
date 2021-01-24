def countDigits( n : int) -> int:
    count = 0
    while n>0:
        n = n//10
        count+=1
    return count

def solution(nums) -> int:
    result = 0
    for n in nums:
        if countDigits(n)%2 == 0: 
            result+=1

    return result

myList = [12,234,89282,3232,0]
print(solution(myList))