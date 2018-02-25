#Hugh O'Reilly,  25/02/18
#Project Euler Problem 5
i = 1
n = i + 1


for i in range(1,21): #defines the range of i
    while i % n == 0:
        print (i)
    
print ("Smallest no. evenly divisible by 1 to 20", i)
