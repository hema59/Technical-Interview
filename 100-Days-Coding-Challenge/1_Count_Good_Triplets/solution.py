
def solution( array : list, a :int, b:int, c:int) -> int:
    arrayLength, count = len(array), 0

    for i in range(arrayLength-2):
        for j in range(i+1, arrayLength-1):
            if abs( array[i]-array[j]) > a : break
            else:
                for k in range(j+1, arrayLength):
                    count += (abs(array[j]-array[k])<=b and abs(array[i]-array[k])<=c)
    return count

array = [3,0,1,1,9,7]
print(solution(array, 7,2,3))
