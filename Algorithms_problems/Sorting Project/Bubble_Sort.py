# Credit https://www.geeksforgeeks.org/bubble-sort/
# Python program for implementation of Bubble Sort 
import time #import time function 
start = time.time() #start time 
def bubbleSort(arr): #bubble sort function
    n = len(arr) #assign n = to length of the array
  
    # Iterate through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # iteratee the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
  
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]), 
end = time.time() #end time
print(end - start) #outputs time to execute method