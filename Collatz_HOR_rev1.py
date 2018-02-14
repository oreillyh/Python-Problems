#Collatz Conjecture Python with user entering positive integer
#Hugh O'Reilly 14/02/18
n = int(input('Enter a number: greater than 1:\n'))

while n > 1:
    if  n % 2 == 0:
        n = (n//2)
        print (n)

    else:
        n = (3*n + 1)
        print(n)

