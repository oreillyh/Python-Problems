#Hugh O'Reilly,  03/03/18
#Project Euler Problem 5 https://projecteuler.net/problem=5
#Solution courtesy of Noa  https://github.com/npradaschnor/52167-Programming-and-Scripting-Exercises/blob/master/ProjEulerProblem5.py

i = 2 #number starts from 2
f = 2 #number that I need to find out

while i < 21: #while the number is 20
  if f % i == 0: #f must be an even number
   i = i + 1 #add 1 to the number
  else: #otherwise
    f=f+1 #add a number to the number I need to find out
    i=2

print('The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:',f) 
        


