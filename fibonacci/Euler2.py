#Euler 2 Solution from https://stackoverflow.com/questions/23258545/project-euler-2-in-python

x = 1
y = 1
z = 0
result = 0

while z < 4000000:
   z = (x+y)         
   if z%2 == 0:
       result = result + z

   #next iteration

   x = y
   y = z

print (result)