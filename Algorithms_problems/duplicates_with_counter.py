import time
start = time.time() #start time
import numpy as np
def contains_duplicates(elements):
    for i in range (0, len(elements)):
        count = 0 #set counter to zero
        for j in range (0, len(elements)):
            count = count  + 1 #increment counter by one for each inner loop iteration
            if i ==j: #avoid self comparison
                continue
            if elements[i] == elements[j]:
                return count# duplicate found
    return False
    
    print(elements)

elements = [1,2,3,4,5,6,6,7,8,9,10] #Duplicate at position 7

print(contains_duplicates(elements))#outputs loop count before duplicate is found
end = time.time() #end time
print(end - start) #outputs time to execute method