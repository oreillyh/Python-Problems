def finder(data): #Function assigns each integer in a list with positional indices
     return finder_rec(data, len(data)-1) # returns each integer in list and it's position
def finder_rec(data,x): #function which recursively sorts data to find largest item
    if x==0: #Checks the number of items in list, if only 1 returns that integer
        return data[x] #returns the position of each integer
    v1 = data[x] #places current integer in list based on its index onto the stack
    v2 = finder_rec(data, x-1)#placeholder for next integer in list, line 6 and 7 sort the data by position. v2 calls the finder_rec function upon itself
    if v1>v2: #compares all values of v1 to v2(finder_rec() called upon itself) 
        return v1 #returns v1 if v1>v2
    else:
        return v2 #returns v2 if v2>v1, v2 is the position for the largest integer during each recursion (This is the termination condition)
print (finder([0, -247, 341, 1001, 741, 22]))