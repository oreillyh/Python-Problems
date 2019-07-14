#Credit https://www.geeksforgeeks.org/bucket-sort-2/
# Python3 program to sort an array  
# using bucket sort  
import time #import time function
import numpy as np
from numpy import mean
from random import randint
import statistics as st 

#number of runs to average
num_runs = 10
results = []# array to hold the results of each run
list = ([10,100,250,500, 1000]) 

#Generate random numbers
def random_array(d):
    array = []
    for i in range (0, 100, 1): #between 0 and 100
        array.append(randint(0,100))# 100 random integers
    return array
    time = []
#Loop to carry out sort on each run
for r in range(num_runs): #Loop to carry out sort on each run
    
        start = time.time() #start time
    def insertionSort(b): #function to create an insertion - needed to sort data once its in buckets
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
            arr[i] = insertionSort(arr[i]) 
            
        # concatenate the result 
        k = 0
        for i in range(slot_num): #for each sorted bucket, add them together
            for j in range(len(arr[i])): 
                x[k] = arr[i][j] 
                k += 1
        return x 
    
# Driver Code 
x = (random_array(d))
print("Sorted Array is") 
print(bucketSort(x)) 
end = time.time() #end time
print(end - start) #outputs time to execute method 
    # This code is contributed by 
    # Oneil Hsiao 