from time import time #
from time import sleep
from numpy.random import randint
import numpy as np
import pandas as pd

#credit: Patrick Mannions GMIT Computational Thinking with algorithms notes
def random_array(n):#create a random array
    array = []
    for i in range (0, n, 1): #between 0 and 100
        array.append(randint(0,100))# 100 random integers
    return array

runs = 10 # number of runs


def Merge_Sort(arr): 
        if len(arr) >1: #Checks for positive integers in the array
            mid = len(arr)//2 #Divides the array in two
            L = arr[:mid] # assigns L as left hand side sub array
            R = arr[mid:] # assigns R as right hand side sub array

            Merge_Sort(L) # Sorts the Left hand side
            Merge_Sort(R) # Sorts the right hand side

            i = j = k = 0 #sets all indices to 0

            # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): #check each item in both subarrays
                if L[i] < R[j]: 
                    arr[k] = L[i] 
                    i+=1
                else: 
                    arr[k] = R[j] 
                    j+=1
                k+=1

            # Checking all elements in Left sub array
            while i < len(L): #While loop to check each item in array
                arr[k] = L[i] 
                i+=1
                k+=1

            # Checking all elements in Right sub array  
            while j < len(R): #While loop to check each item in array
                arr[k] = R[j] 
                j+=1 
                k+=1

b = random_array(1)
results=[] # Array to store times

l = [10,100,250,500,1000, 10000, 100000] # array containing array size to sort
for i in l:
    for runs in range(runs): # iterate through each run
        start=time() # set the start time
        # use sorting routine
        Merge_Sort(b)
        end=time() #set the end time
        elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
        results.append(elapsed)
        average =np.average(elapsed) # average using numpy
#df = pd.DataFrame('average')
print(average)
    # print('Average Time Taken: %10f ms' % (average),'{0:2d} {1:3d} {2:4d} {3:5} {4:6} {5:7}'.format(10,100,250,500,1000,10000, end = ' '))

