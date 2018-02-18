# Hugh O'Reilly 18-Feb-2018
# A program that solves problem 2 on project euler
# Finds the sum of the even valued terms of the Fibonacci sequence less the 4 million.

def fib(n):
  
  i = 0
  j = 1
  n = n - 1

  while n <= 4000000:
    i, j = j, i + j
    n += 1
    if n % 2 == 0:
      append(n)
  print(n)



  
  

