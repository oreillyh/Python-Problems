# Hugh O'Reilly 
    # 05/03/18
    # Defining a function to return the Factorial of an integer
n = int(input('Enter a number: greater than 1:\n')) #prompts user to input integer
def factorial(n):# defines the function n
    if n > 1: return n * factorial(n - 1) #calculates factorial
    elif n >= 0: return 1 #factorial is 1 if n is 0
    else: return ('n/a') #returns n/a for neg number input
print ('The factorial of n is', factorial(n)) #prints output


    