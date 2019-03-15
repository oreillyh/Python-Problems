def Sequential_Search(elements):
    pos = 0
    for i in range (0, len(elements)):
        for j in range(0, len(elements)):
            if i == j:
                continue
            else:
                if pos < len(elements) and elements[i] == elements[j]:
                    pos = pos + 1
    return pos
elements = [1,2,3,4,5,6,6,7,8,9,10]
print(Sequential_Search(elements))