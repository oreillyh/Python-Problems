def Sequential_Search(elements):
    count = 0 #set counter to zero to initialise
    for i in range (0, len(elements)): #outer loop for comparison
        for j in range (0, len(elements)):#inner loop to compare against outer loop
            count = count + 1 #increments counter
            if i == j:
                continue #avoids self comparison
            while count < len(elements) and elements[i] != elements[j]:# counts 'itertations' of inner loop until condition met
                
                return count #returns count until condition met
elements = [1,2,3,4,5,6,6,7,8,9,10]
print (Sequential_Search(elements))