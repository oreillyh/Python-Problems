def factorial(n):
    factorial = 1;
    for i in range(2,n+1):
        factorial = factorial * i
    return factorial
print(factorial(5))
