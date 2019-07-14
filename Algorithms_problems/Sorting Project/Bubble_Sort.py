# Credit https://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
# Python program for implementation of Bubble Sort 
# Credit https://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
# Python program for implementation of Bubble Sort 
import time #import time function
import numpy as np
from numpy import mean
from random import randint
import statistics as st 

#number of runs to average
runs = 10
results = []# array to hold the results of each run
list = ([10,100,250,500, 1000])

#Genarate random numbers
def random_array(n):
    array = []
    for i in range (0, 100, 1): #between 0 and 100
        array.append(randint(0,100))# 100 random integers
    return array

#Loop to carry out sort on each run
for r in range(runs): 
        start = time.time() #start time  
        b = random_array(n)
        def Bubble_Sort(b):
            for passnum in range(len(b)-1,0,-1):
                for i in range(passnum):
                    if b[i]>b[i+1]:
                        temp = b[i]
                        b[i] = b[i+1]
                        b[i+1] = temp

        Bubble_Sort(b)
        end = time.time() #end time
        elapsed = end - start #outputs time to execute method
        results.append(elapsed)
        average = np.mean(elapsed)
        print('Time Taken: %10f s' % (average))