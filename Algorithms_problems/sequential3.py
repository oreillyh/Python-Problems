def Sequential_Search(elements):
    for i in range (len(elements)): #outer loop for comparison
        for j in range (len(elements)):#inner loop to compare against outer loop
            pos = 0
            found = False
            while pos < len(elements) and not found:
                if j == i:
                    continue
                else:
                    pos = pos + 1
            return found, pos
elements = [1,2,3,4,5,6,6,7,8,9,10]
print(Sequential_Search(elements))