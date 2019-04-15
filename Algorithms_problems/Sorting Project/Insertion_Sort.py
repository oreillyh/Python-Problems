import time #import time function 
start = time.time() #start time
#credit https://www.pythoncentral.io/insertion-sort-implementation-guide/
def insertion_Sort(alist):
    for i in range(1,len(alist)): #for each element in thr list to be sorted
        #element to be compared
        current = alist[i] 
        #comparing the current element with the sorted portion and swapping
        while i>0 and alist[i-1]>current: #compare each element with the previous one
            alist[i] = alist[i-1]
            i = i-1
            alist[i] = current #swap replaced element with current one
    return alist
print(insertion_Sort([7,1,3,5,9,2,3]))
end = time.time() #end time
print(end - start) #outputs time to execute method