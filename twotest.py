
def contains duplicates(elements):
    for i in range(0, len(elements)):
        for j in range(0, len(elements)):
            if i ==j:
                continue
            if elements[i] == elements[j]:
                return True
    return False

test1 = [0,2,1,2]
test2 = [1,2,3,4]

print(contains duplicates(test1))
print(contains duplicates(test2))