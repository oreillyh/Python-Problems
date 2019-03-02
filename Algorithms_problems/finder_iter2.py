def findmax(data):

    if len(data) == 0:
        return 0

    curr_max = data[0]

    for i in data:
        if i > curr_max:
            curr_max = i

    return curr_max
data = [0,-247,341,1001,741,22]
print(findmax(data))

