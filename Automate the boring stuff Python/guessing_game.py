from random import randint
for i in range(5):
    guess = int(input("Enter a number between 1 and 10\n"))
    randNum = randint(1,10)
    if guess ==randNum:
        print("We matched")
        break
    else:
        print("We did not match. Try again")
