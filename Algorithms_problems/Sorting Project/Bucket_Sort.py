#Credit https://www.geeksforgeeks.org/bucket-sort-2/
# Python3 program to sort an array  
# using bucket sort  
import time #import time function 
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
x = [0.897, 0.565, 0.656, 
     0.1234, 0.665, 0.3434]  
print("Sorted Array is") 
print(bucketSort(x)) 
end = time.time() #end time
print(end - start) #outputs time to execute method 
# This code is contributed by 
# Oneil Hsiao 