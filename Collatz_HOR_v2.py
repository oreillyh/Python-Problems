#Collatz Conjecture Python with user entering positive integer
#Hugh O'Reilly 14/02/18
n = int(input('Enter a number: greater than 1:\n')) #Int command makes sure integer is whole, \n ensures data entry is on next line

while n > 1:
    if  n % 2 == 0:
        n = (n//2)
        print (n)

    else:
        n = (3*n + 1)
        print(n)

