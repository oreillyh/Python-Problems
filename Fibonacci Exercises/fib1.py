# Hugh O'Reilly
# 06/04/2018
# Fibonacci series: up to 100
# the sum of two elements defines the next
a, b = 0, 1
while b < 100:
  print(b)
  a, b = b, a+b
#Fibonacci sequence calculated by adding a and b and returning b back into a's position, 
# iterated for each number in fib sequence
