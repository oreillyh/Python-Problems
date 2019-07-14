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

### Bubble_Sort Code

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


### Merge_Sort Code

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
b = random_array(n)
results=[] # Array to store times
Sort_Functions = {Bubble_Sort, Counting_Sort, Merge_Sort, Insertion_Sort}
for i in Sort_Functions:
    l = [10,100,250,500,1000, 10000, 100000] # array containing array size to sort
    for i in l:
        for runs in range(runs): # iterate through each run
            start=time() # set the start time
            # use sorting routine
            Merge_Sort(b)
            end=time() #set the end time
            elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
            results.append(elapsed)
            #print('sort times: ', elapsed) # so you can see the list grow
        #then outside of the loop average the list
        average =np.average(elapsed) # average using numpy
        print('Average Time Taken: %10f ms' % (average),'{0:2d} {1:3d} {2:4d} {3:5} {4:6} {5:7}'.format(10,100,250,500,1000,10000, end = ' '))


### Counting_Sort Code

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
        elapsed = (end-start)*1000 #elapsed time multiplied by 1000 for milliseconds
        results.append(elapsed)
        #code to get average using numpy.average
     average = np.average(elapsed) # average using numpy
     print('Average Time Taken: %10f ms' % (average)) #average time in milliseconds

##Insertion_Sort Code

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
b = random_array(1)
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
print('Average Time Taken: %10f s' % (average)) #average time in milliseconds

if __name__ == '__main__':
    
    types={bs:'  Bubble_Sort', ms:'   Merge_Sort', cs:'Counting_Sort', ins:'Insertion_Sort', bks:'Bucket_Sort'}
    headers='ArraySize'
    for key in types:
        headers+=', '+ types[key].strip()
    print(headers)
    valstrArr=[] ##store the rows for saving to a csv file
   
    # loop through the values in the array t and use the value to create an array of random values
    for t in (100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000): 
   
        test = randint(1,t*2,t)
        #print('  Input len,min,max: ', len(test),',',min(test),',',max(test))
        funcAvgTim=[] # create an emty array for storing the average times
        # read the sort types to complete from the types list
        for sortfunc, funcname in types.items():
            times=[] # create an empty list to store the times in fr the cycles
            for i in range(10): # repeat tests to get better average
                #print('         Test Cycle: ',i)
                start=time() # mark the start time of the test
                arr=test.copy() #copy the test array created above and re-use for every following test
                #print('  input: ', arr)
                ret=sortfunc(arr) # run the sort function and return the sorted result
                #print(' sorted: ', ret)
                end=time() # record the end time of the test
                #print(funcname,' time: ',(end-start)*1000)
                times.append((end-start)*1000) # append the test time to the times list
            print (t, funcname, np.average(times)) # prnt the average time to the screen
            funcAvgTim.append(np.average(times)) # save the avarage time to a list for saviing to file 
        valstr='' # initiate a val string for writing to file
        sep='' # nitiate the seperator for seperation of the values
        for val in funcAvgTim:
            valstr+=sep+str(val) # ppend the values to the string to write out to files
            sep=', ' # add the seperator
        #print('{}{}{}'.format(t,sep,valstr))
        valstrArr.append('{}{}{}'.format(t,sep,valstr)) #append the strin to a list for saving below

    for line in valstrArr:
        #print(line) # print the result to screen for validation purposes
        pass

    #write the cycle test resuts to file
    with open('sort_cycle_times_100-10k_by_10cycles.csv', 'w') as file:
        file.write(headers+'\n') # write a header line
        for line in valstrArr: # loop through the lines in the list
            file.write(line+'\n') # and write them out to the file 