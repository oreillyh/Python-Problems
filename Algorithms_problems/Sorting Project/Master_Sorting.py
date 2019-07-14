# Credit https://www.geeksforgeeks.org/bubble-sort/
# Python program for implementation of Bubble Sort 
from time import time #
from time import sleep
from numpy.random import randint #Generate random numbers
import numpy as np
import numpy as np 


#credit: Patrick Mannions GMIT Computational Thinking with algorithms notes
def random_array(n):
    # create an array variable
    array = []
    for i in range(0, n, 1):
        # add to the array random integers between 0 and 100
        array.append(randint(0,100))
    return array


###BUBBLE SORT

# Credit https://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
# Python program for implementation of Bubble Sort 
# Credit https://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
# Python program for implementation of Bubble Sort 
def Bubble_Sort(b):
    for passnum in range(len(b)-1,0,-1):
        for i in range(passnum):
            if b[i]>b[i+1]:
                temp = b[i]
                b[i] = b[i+1]
                b[i+1] = temp

###BUCKETSORT

#Credit https://www.geeksforgeeks.org/bucket-sort-2/
# Python3 program to sort an array  
# using bucket sort  
def Insertion_Sort(b): #function to create an insertion - needed to sort data once its in buckets
    for i in range(1, len(b)): #iterate through all the data
        up = b[i] 
        j = i - 1
        while j >=0 and b[j] > up:
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up     
    return b      
              
def bucketSort(x): #create buckets
    arr = [] #empty array
    slot_num = 10 # 10 means 10 slots, each 
                  # slot's size is 0.1 
    for i in range(slot_num): #for each slot number
        arr.append([]) #append slot numbers to the array
          
    # Put array elements in different buckets  
    for j in x: 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 
      
    # Sort individual buckets  using the insertion sort created earlier
    for i in range(slot_num): 
        arr[i] = Insertion_Sort(arr[i]) 
          
    # concatenate the result 
    k = 0
    for i in range(slot_num): #for each sorted bucket, add them together
        for j in range(len(arr[i])): 
            x[k] = arr[i][j] 
            k += 1
    return x 
  
###INSERTION SORT 

def Insertion_Sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

###COUNTING SORT

# This code is contributed by 
# Oneil Hsiao 

# Credit https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
def Counting_Sort(array1, max_val): # function for counting sort, takes an array and a max value
    m = max_val + 1 #assigns m as max value +1: needed to create index for count sub-array 'count'
    count = [0] * m  #sub array to hold the counts for each element of the array              
    
    for a in array1: #loop which iterates through each item in the array
    
        count[a] += 1 # count occurences of each element             
    i = 0
    for a in range(m): #Outer sorting loop to iterate through count sub-array           
        for c in range(count[a]):  #inner sorting loop which iterates through the counts of each element
            array1[i] = a #sorts elements by swapping count items
            i += 1 #increases position of count item to be sorted 
    return array1

#credit https://www.pythoncentral.io/insertion-sort-implementation-guide/
def Insertion_Sort(alist):
    for i in range(1,len(alist)): #for each element in thr list to be sorted
        #element to be compared
        current = alist[i] 
        #comparing the current element with the sorted portion and swapping
        while i>0 and alist[i-1]>current: #compare each element with the previous one
            alist[i] = alist[i-1]
            i = i-1
            alist[i] = current #swap replaced element with current one
    return alist


###MERGE SORT

#Credit This code is contributed by Mayank Khanna @ https://www.geeksforgeeks.org/merge-sort/
# Python program for implementation of MergeSort 

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

import pandas as pd
# import time module
from time import time #
from time import sleep
from numpy.random import randint
import numpy as np

#array sizes
array50 = random_array(50)
array100 = random_array(100)
array250 = random_array(250)
array500 = random_array(500)
array1000 = random_array(1000)
array10000 = random_array(10000)

# function to call sort functions and time each individually
    
# BUBBLE SORT

num_runs = 10
results = []
#array 50
for r in range(num_runs):
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array50)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Bubble_Sort_50_Average = np.average(elapsed) # average using numpy
print('Bubble_Sort 50 Time Taken: %10f ms' % (Bubble_Sort_50_Average)) #average time in milliseconds

#array 100
for r in range(num_runs): #iterate through each run
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array100)
    end=time() #set the end time
    elapsed = (end-start)*1000
    results.append(elapsed)
    #code to get average using numpy.average
    Bubble_Sort_100_Average = np.average(elapsed) # average using numpy
print('Bubble_Sort 100 Time Taken: %10f ms' % (Bubble_Sort_100_Average)) #average time in milliseconds

#array 250
for r in range (num_runs): #iterate through each run
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array250)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Bubble_Sort_250_Average = np.average(elapsed) # average using numpy
print('Bubble_Sort 250 Time Taken: %10f ms' % (Bubble_Sort_250_Average)) #average time in milliseconds

#array 500
for r in range(num_runs): #iterate through each run
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array500)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Bubble_Sort_500_Average = np.average(elapsed) # average using numpy
print('Bubble_Sort 500 Time Taken: %10f ms' % (Bubble_Sort_500_Average)) #average time in milliseconds

#array 1000        
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array1000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
     #code to get average using numpy.average
    Bubble_Sort_1000_Average = np.average(elapsed) # average using numpy
print('Bubble_Sort 1000 Time Taken: %10f ms' % (Bubble_Sort_1000_Average)) #average time in milliseconds

#array 10000
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array10000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
     #code to get average using numpy.average
    Bubble_Sort_10000_Average = np.average(elapsed) # average using numpy
print('Bubble_Sort 10000 Time Taken: %10f ms' % (Bubble_Sort_10000_Average)) #average time in milliseconds 

##### Merge Sort
    
    #array 50

for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array50)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_50_Average = np.average(elapsed) # average using numpy
print('Merge_Sort 50 Time Taken: %10f ms' % (Merge_Sort_50_Average)) #average time in milliseconds
        
        
    #Array 100       
  
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array100)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_100_Average = np.average(elapsed) # average using numpy
print('Merge_Sort 100 Time Taken: %10f ms' % (Merge_Sort_100_Average)) #average time in milliseconds
    
          
    #array 250
    
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array250)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_250_Average = np.average(elapsed) # average using numpy
print('Merge_Sort 250 Time Taken: %10f ms' % (Merge_Sort_250_Average)) #average time in milliseconds
    
   
    #array 500

for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array500)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_500_Average = np.average(elapsed) # average using numpy
print('Merge_Sort 500 Time Taken: %10f ms' % (Merge_Sort_500_Average)) #average time in milliseconds
        
   
    #array 1000

for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array1000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_1000_Average = np.average(elapsed) # average using numpy
print('Merge_Sort 1000 Time Taken: %10f ms' % (Merge_Sort_1000_Average)) #average time in milliseconds

    #array 10000
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array10000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_10000_Average = np.average(elapsed) # average using numpy
print('Merge_Sort 10000 Time Taken: %10f ms' % (Merge_Sort_10000_Average)) #average time in milliseconds

##### Insertion Sort

for r in range(num_runs): # iterate through each run
    start=time() # set the start time
     # use sorting routine
    Insertion_Sort(array50)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_50_Average = np.average(elapsed) # average using numpy
print('Insertion_Sort 50 Time Taken: %10f ms' % (Insertion_Sort_50_Average)) #average time in milliseconds
    
    
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Insertion_Sort(array100)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_100_Average = np.average(elapsed) # average using numpy
print('Insertion_Sort 100 Time Taken: %10f ms' % (Insertion_Sort_100_Average)) #average time in milliseconds
   
    
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Insertion_Sort(array250)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_250_Average = np.average(elapsed) # average using numpy
print('Insertion_Sort 250 Time Taken: %10f ms' % (Insertion_Sort_250_Average)) #average time in milliseconds
    
    
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Insertion_Sort(array500)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_500_Average = np.average(elapsed) # average using numpy
print('Insertion_Sort 500 Time Taken: %10f ms' % (Insertion_Sort_500_Average)) #average time in milliseconds            
    
   
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Insertion_Sort(array1000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_1000_Average = np.average(elapsed) # average using numpy
print('Insertion_Sort 1000 Time Taken: %10f ms' % (Insertion_Sort_1000_Average)) #average time in milliseconds

for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Insertion_Sort(array10000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_10000_Average = np.average(elapsed) # average using numpy
print('Insertion_Sort 10000 Time Taken: %10f ms' % (Insertion_Sort_10000_Average)) #average time in milliseconds

#Credit https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
# Creation of  simple Pandas array of the data
#import the pandas library
import pandas as pd
# import time module
from time import time #
from time import sleep

#credit https://www.numpy.org/
from numpy.random import randint
import numpy as np

#array sizes
array50 = random_array(50)
array100 = random_array(100)
array250 = random_array(250)
array500 = random_array(500)
array1000 = random_array(1000)
array10000 = random_array(10000)

# function to call sort functions and time each individually
    
# BUBBLE SORT

num_runs = 10

#array 50
for r in range(num_runs):
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array50)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Bubble_Sort_50_Average = np.average(elapsed) # average using numpy


#array 100
for r in range(num_runs): #iterate through each run
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array100)
    end=time() #set the end time
    elapsed = (end-start)*1000
    results.append(elapsed)
    #code to get average using numpy.average
    Bubble_Sort_100_Average = np.average(elapsed) # average using numpy


#array 250
for r in range (num_runs): #iterate through each run
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array250)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Bubble_Sort_250_Average = np.average(elapsed) # average using numpy


#array 500
for r in range(num_runs): #iterate through each run
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array500)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Bubble_Sort_500_Average = np.average(elapsed) # average using numpy


#array 1000        
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array1000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
     #code to get average using numpy.average
    Bubble_Sort_1000_Average = np.average(elapsed) # average using numpy


#array 10000
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Bubble_Sort(array10000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
     #code to get average using numpy.average
    Bubble_Sort_10000_Average = np.average(elapsed) # average using numpy


##### Merge Sort
    
    #array 50

for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array50)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_50_Average = np.average(elapsed) # average using numpy

        
        
    #Array 100       
  
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array100)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_100_Average = np.average(elapsed) # average using numpy

    
          
    #array 250
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array250)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_250_Average = np.average(elapsed) # average using numpy

    
   
    #array 500
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array500)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_500_Average = np.average(elapsed) # average using numpy

        
   
    #array 1000
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array1000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_1000_Average = np.average(elapsed) # average using numpy

    #array 10000
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Merge_Sort(array10000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Merge_Sort_10000_Average = np.average(elapsed) # average using numpy


##### Insertion Sort

for r in range(num_runs): # iterate through each run
    start=time() # set the start time
     # use sorting routine
    Insertion_Sort(array50)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_50_Average = np.average(elapsed) # average using numpy

    
    
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Insertion_Sort(array100)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_100_Average = np.average(elapsed) # average using numpy

   
    
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Insertion_Sort(array250)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_250_Average = np.average(elapsed) # average using numpy

    
    
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Insertion_Sort(array500)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_500_Average = np.average(elapsed) # average using numpy
        
    
   
for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Insertion_Sort(array1000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_1000_Average = np.average(elapsed) # average using numpy


for r in range(num_runs): # iterate through each run
    start=time() # set the start time
    # use sorting routine
    Insertion_Sort(array10000)
    end=time() #set the end time
    elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
    results.append(elapsed)
    #code to get average using numpy.average
    Insertion_Sort_10000_Average = np.average(elapsed) # average using numpy


# Create a pandas dataframe using the Pandas Library
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

df = pd.DataFrame(columns = ['Array Size', 'Bubble_Sort', 'Merge_Sort']) #define the column names
df ['Array Size'] = [50, 100, 250, 500, 1000, 10000] # define the inout for the array size column

#define the output for each array
df['Bubble_Sort'] = Bubble_Sort_50_Average, Bubble_Sort_100_Average, Bubble_Sort_250_Average, Bubble_Sort_500_Average, Bubble_Sort_1000_Average, Bubble_Sort_10000_Average
df['Merge_Sort'] = Merge_Sort_50_Average, Merge_Sort_100_Average, Merge_Sort_250_Average, Merge_Sort_500_Average, Merge_Sort_1000_Average, Merge_Sort_10000_Average
df['Insertion_Sort'] = Insertion_Sort_50_Average, Insertion_Sort_100_Average, Insertion_Sort_250_Average, Insertion_Sort_500_Average, Insertion_Sort_1000_Average, Insertion_Sort_10000_Average

df #output the dataframe

#credit https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot
# https://matplotlib.org/
#Plot the arrays vs runtime using the seaborn and matplotlib packages
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
warnings.simplefilter(action='ignore', category=FutureWarning) #Workaround to remove 'FutureWarnings' message which appears to be a bug.
#set the output styles dark background and the size of the plot
sns.set(style="darkgrid",rc={'figure.figsize':(20,20)})

# Merge sort plot in seaborn, define x and y variables and labels for each line
#https://seaborn.pydata.org/generated/seaborn.lineplot.html#seaborn.lineplot

sns.lineplot( x="Array Size", y="Merge_Sort",data = df, label='Merge Sort')
# Insertion sort plot in seaborn
sns.lineplot( x="Array Size", y="Insertion_Sort", data = df, label="Insertion Sort")
# Bubble Sort plot in seaborn
sns.lineplot( x="Array Size", y="Bubble_Sort", data = df, label='Bubble Sort')

#add title
title="Sorting Algorithms: Benchmarking Run Time v Array Size"

#add x and y labels using matplotlib
plt.xlabel('Array Size', fontsize=19)
plt.ylabel('Run Time(s)',fontsize=19)


    
#add title
plt.title(title, fontsize=32)

#output plot

plt.show()

