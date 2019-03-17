import time #import time function 
start = time.time() #start time
import numpy as np
def contains_duplicates(elements):
    for i in range (0, len(elements)):
        for j in range (0, len(elements)):
            if i == j: #avoid self comparison
                continue
            if elements[i] == elements[j]:
                return True #duplicate found
    return False
    
    #print(elements)

elements = [0,1,0,-127,346,125]
    
 
print(contains_duplicates(elements))
end = time.time() #end time
print(end - start) #outputs time to execute method