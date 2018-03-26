def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1
# lines 1-5 creates a function'fib' to calculate the Fibonacci no of n
  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i
#lines 7 to 11 defines while loop when n is greater than 0, adding sum of i and j and returns i whcih is the nth fibonacci number

#Text for Homework Week 2
#My surname is O'Reilly
#The first letter O is number 79
#The last letter y is number 121
#Fibonacci number 200 is 280571172992510140037611932413038677189525
# ord() Returns an integer which is assigned to a unicode string character. Its inverse the chr() function returns a string character to an integer

name = "O'Reilly"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno
# lines 14 to 19 create integers from the strings of the 1st and last letters in my name
ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
# lines 22 -25 requests user input of their name, and prints fibonacci number,
# x which is the sum of integers created by 1st and last letters of name.
