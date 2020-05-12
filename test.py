x = [1,2,3,4,5,6]

square = lambda x: x * x
#def square(num):
    #return num*num
result = map(square, x)

print(result)

print(map(square, result))
