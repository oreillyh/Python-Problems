#Hugh O'Reilly, 2018-02-11 uploaded and cloned
#FizzBuzz: https://en.wikipedia.org/wiki/Fizz_buzz

i = 1

while i <= 10:
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print ("buzz")
    else:
        print(i)
    i=i+1