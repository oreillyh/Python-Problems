#credit https://en.wikibooks.org/wiki/Algorithms/Find_maximum/Python_method_1

def finder(data): #function to iteratively find maximun in an array

    if len(data) == 0: #condition if no items in list (max=0)
        return 0

    curr_max = data[0] #assigns current item in array as max]

    for i in data:#loops through items in array
        if i > curr_max:#checks each item in array against current max
            curr_max = i #assigns new value of i as max
            
    return curr_max #outputs max value
data = [0,-247,341,1001,741,22]
print(finder(data))

