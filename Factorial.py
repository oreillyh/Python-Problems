# Hugh O'Reilly 
    # 05/03/18
    # Defining a function to return the Factorial of an integer
n = int(input('Enter a number greater than 1:\n')) #prompts user to input integer
def factorial(n):# defines the function n
    if n == 0: return 1 #factorial is 1 if n is 0
    else: return n * factorial(n - 1) #calculates factorial
print ('The factorial of your number is', factorial(n)) #prints output


    