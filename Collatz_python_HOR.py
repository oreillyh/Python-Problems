#Collatz Conjecture Python
i = 17
i = (i - 1)
while  i % 2 == 0:
    print(i-1)
    i = (i//2)
else:
    print(i)
    i=(3*i + 1)
