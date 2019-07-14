from time import time #
from time import sleep
from numpy.random import randint
import numpy as np

#credit: Patrick Mannions GMIT Computational Thinking with algorithms notes
def random_array(n):#create a random array
    array = []
    for i in range (0, 100, 1): #between 0 and 100
        array.append(randint(0,100))# 100 random integers
    return array

runs =10 # number of runs

a = random_array(n)
def Insertion_Sort(a):
    for i in range(1,len(a)): #for each element in the list to be sorted
        #element to be compared
        current = a[i] 
        #comparing the current element with the sorted portion and swapping
        while i>0 and a[i-1]>current: #compare each element with the previous one
            a[i] = a[i-1]
            i = i-1
            a[i] = current #swap replaced element with current one
        return a

#Credit This code is adapted from code by Mayank Khanna @ https://www.geeksforgeeks.org/merge-sort/
b = random_array(n)
sort_times=[] # Array to store times
#Sort_Functions = {Bubble_Sort, Counting_Sort, Merge_Sort, Insertion_Sort}
l = [10,100,250,500,1000,10000] # array containing array size to sort
for i in l:
        for runs in range(runs): # iterate through each run
            start=time() # set the start time
            # use sorting routine
            Insertion_Sort(b)
            end=time() #set the end time
            elapsed = (end-start)*1000
            results.append(elapsed)
            #print('sort times: ', elapsed) # so you can see the list grow
            #Average the runs
            average =np.average(elapsed) # average using numpy
print('Average Time Taken: %10f ms' % (average),'{0:2d} {1:3d} {2:4d} {3:5} {4:6} {5:7}'.format(10,100,250,500,1000,10000, end = ' '))
