import numpy as np
def contains_duplicates(elements):
    for i in range (0, len(elements)):
        for j in range (0, len(elements)):
            if i ==j: #avoid self comparison
                continue
            if elements[i] == elements[j]:
                return True # duplicate found
    return False
    
    print(elements)

elements = [1,2,3,4,5,6,7,8,9,10,10]

#np.random.random_integers(10, size=(10)) #generates 100 random integers between 1 and 10

print(contains_duplicates(elements))

