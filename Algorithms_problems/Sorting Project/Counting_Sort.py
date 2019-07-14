# Credit https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
from time import time #
from time import sleep
from numpy.random import randint
import numpy as np

#credit: Patrick Mannions GMIT Computational Thinking with algorithms notes
def random_array(n):#create a random array
    array = [] # temporary array
    for i in range (0, n, 1): #numbers between 0 and 100
        array.append(randint(0,100))# append the 100 random integers to the array
    return array

runs = 10 # number of runs per array


def Counting_Sort(a, max_val): # function for counting sort, takes an array and a max value
        m = max_val + 1 #assigns m as max value +1: needed to create index for count sub-array 'count'
        count = [0] * m  #sub array to hold the counts for each element of the array              
    
        for b in a: #loop which iterates through each item in the array
    
            count[b] += 1 # count occurences of each element             
        i = 0
        for b in range(m): #Outer sorting loop to iterate through count sub-array           
            for c in range(count[b]):  #inner sorting loop which iterates through the counts of each element
                a[i] = b #sorts elements by swapping count items
                i += 1 #increases position of count item to be sorted 
        return a

#Credit This code is adapted from code by Mayank Khanna @ https://www.geeksforgeeks.org/merge-sort/
if __name__ == '__main__': #main method to create sort times for sorting algorithm 
    b = random_array(1)
results =[] # Array to store times
l = [10,100,250,500,1000, 10000, 100000] # array containing array size to sort
for i in l:
     for runs in range(runs): # iterate through each run
        start=time() # set the start time
        # use sorting routine
        Counting_Sort(b,100)
        end=time() #set the end time
        elapsed = (end-start) #elapsed time multiplied by 1000 for milliseconds
        results.append(elapsed)
        #code to get average using numpy.average
     average = np.average(elapsed) # average using numpy
     print('Average Time Taken: %10f ms' % (average)) #average time in milliseconds