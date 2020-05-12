def fib(n):
    if (n==1 or n==0):
        return n
    print("we are trying to calculate fib(",n,") we will call fib(",n-1,") fib(",n-2,")")
    return fib(n-1) + fib(n-2)

for i in range(1,10):
    print (fib(i))
