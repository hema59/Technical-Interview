def mergesort( array):
    if len(array) > 1 :
        mid = len(array)//2
    else:
        return False

    left = array[ : mid]
    right = array[ mid :]

    mergesort(left)
    mergesort(right)

    i=j=k=0

    while i <len(left) and j<len(right):
        if left[i] < right[j]:
            array[k]=left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1
        k+=1

    while i < len(left):
        array[k] = left[i]
        i+=1
        k+=1
    
    while j < len(right):
        array[k] = right[j]
        j+=1
        k+=1

    return array

my_array = [8,4,5,6,2,5,4,1,-0]
print("Before: ", my_array)
print("After : ", end = "")
print(mergesort(my_array))