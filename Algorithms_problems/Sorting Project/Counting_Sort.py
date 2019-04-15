# Credit https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
import time #import time function 
start = time.time() #start time 
def counting_sort(array1, max_val): # function for counting sort, takes an array and a max value
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

print(counting_sort( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))
end = time.time() #end time
print(end - start) #outputs time to execute method