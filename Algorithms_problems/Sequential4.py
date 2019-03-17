def Sequential_Search(elements):
    for index, item in enumerate(elements): #outer loop for comparison
        for index, item in enumerate(elements):#inner loop to compare against outer loop
            pos = 0
            while index < item and item == item:
                pos = pos + 1
            return pos
elements = [1,2,3,4,5,6,6,7,8,9,10]
print(Sequential_Search(elements))