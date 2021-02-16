import time

def factorial( n ):
    if n == 1 : return 1
    return factorial(n-1)*n

def is_prime(n):
    if n in (2,3): return True
    for i in range( 2, n):
        if n%i == 0 :
            return False
    return True

def all_primes_in( n : int) -> list:
    for i in range(1, n+1):
        if is_prime(i) == True:
            print(i, end = " ")

def fibonacci( n ):
    if n < 0 : print("Invalid")
    elif n == 0 : 
        return 0 
    elif n == 1 or n == 2 : 
        return 1 
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib = [0,1]
def dp_fibonacci( n ):
    if n <=0: print("Invalid")
    if n <= len(fib):
        return fib[n-1]
    else:
        t_fib = dp_fibonacci(n-1)+dp_fibonacci(n-2)
        fib.append(t_fib)
        return t_fib



start = time.time()
print("Factorial of 5", factorial(4))
print(f"Completed in {start - time.time(): 0.4f} ")


start = time.time()
print("Primes in [1, 35]", all_primes_in(35))
print(f"Completed in {start - time.time(): 0.4f} ")

start = time.time()
result1 = fibonacci(19-1)
print("9th number in the Fibonacci series", result1 )
print(f"Completed in {start - time.time(): 0.4f} ")

start = time.time()
result = dp_fibonacci(19)
print("9th number in the Fibonacci series", result )
print(f"Completed in {start - time.time(): 0.4f} ")

for i in range(1,20):
    print("{0}th fibonacci number is {1}".format(i,dp_fibonacci(i)))