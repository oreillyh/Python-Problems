def contains_duplicates(elements):
    for i in range(0, len(elements)):
        for j in range(0, len(elements)):
            if i == j: 
                continue
        count = 0       
        while elements[i] == elements[j]:
                count = count +1 # duplicate found
                print(count)
    
    print(elements)

elements = [1,2,3,4,5,6,6,7,8,9,10] #Best case where first pair have duplicates

#elements =  np.arange(1,1001) #generates 100 random integers between 1 and 10

print(contains_duplicates(elements))
