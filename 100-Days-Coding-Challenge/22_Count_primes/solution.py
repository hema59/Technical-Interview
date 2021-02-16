def is_prime(num):
    if num in (2,3): return True
    i = 2
    while i < num:
        if num%i == 0 : return False
        else:
            i+=1
    return True



def find_primes(n:int) -> list:
    array = []
    for i in range(2, n+1):
        if is_prime(i) == True: 
            array.append(i)
    return array

import time
start = time.time()


print("Primes in range 1 and 50 : ",find_primes(50) )
print(f"Completed in {start - time.time(): 0.9f}")