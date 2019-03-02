def contains_duplicates(elements):
    for i in range (0, len(elements)):
        for j in range (0, len(elements)):
            if i ==j: #avoid self comparison
                continue
            if elements[i] == elements[j]:
                return True # duplicate found
    return False

elements = [1,2,45,66,76,55,2,45,37,66]

print(contains_duplicates(elements))