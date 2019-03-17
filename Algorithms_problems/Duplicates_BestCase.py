import time #import time function 
start = time.time() #start time
import numpy as np
def contains_duplicates(elements):
    for i in range (0, len(elements)):
        for j in range (0, len(elements)):
            if i ==j: #avoid self comparison
                continue
            if elements[i] == elements[j]:
                return True# duplicate found
    return False
    
    print(elements)

elements = [1,1,2,3,4] #Best case where first pair have duplicates

#elements =  np.arange(1,1001) #generates 100 random integers between 1 and 10

print(contains_duplicates(elements))
end = time.time() #end time
print(end - start) #outputs time to execute method