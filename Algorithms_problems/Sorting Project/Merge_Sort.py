#Credit This code is contributed by Mayank Khanna @ https://www.geeksforgeeks.org/merge-sort/
# Python program for implementation of MergeSort 
import time #import time function 
start = time.time() #start time
def mergeSort(arr): 
    if len(arr) >1: #Checks for positive integers in the array
        mid = len(arr)//2 #Divides the array in two
        L = arr[:mid] # assigns L as left hand side sub array
        R = arr[mid:] # assigns R as right hand side sub array
  
        mergeSort(L) # Sorts the Left hand side
        mergeSort(R) # Sorts the right hand side
  
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
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
end = time.time() #end time
print(end - start) #outputs time to execute method
