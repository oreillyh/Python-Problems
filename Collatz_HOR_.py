#Collatz Conjecture Python
#demonstrated the use of python to calculate the collatz conjecture on 17
#Hugh O'Reilly 12/02/18
n = 17 # n assigned assigned the value of 17

while n > 1: #while loop to define the conditions of n and create output based on odd or even iterations
    if  n % 2 == 0: #if statement creates function when n is even
        n = (n//2)
        print (n)

    else: # else statement creates function when n is not even
        n = (3*n + 1)
        print(n)

