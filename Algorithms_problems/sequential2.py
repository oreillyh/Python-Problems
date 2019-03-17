def Sequential_Search(elements):
        for i in range (0, len(elements)): #outer loop for comparison
        count = 0  #set counter to zero to initialise
        for j in range(0, len(elements)):#inner loop to compare against outer loop
            if i == j:
                continue #avoids self comparison
            if elements[i] != elements[j]:# counts 'iterations' of inner loop until condition met
                count = count + len(elements) #increments counter
                else if elements[i] == elements[j]:
                    count = count +1
    return count #returns count until condition met
elements = [1,2,3,4,5,6,6,7,8,9,10]
print (Sequential_Search(elements))