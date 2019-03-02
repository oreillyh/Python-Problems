def finder(data): #Function which recursively compares each integer in a list to find largest, i.e. the function is called upon itself unitil the base condition is met (v2>v1)
     return finder_rec(data, len(data)-1) # returns each integer in list and it's position
def finder_rec(data,x): #function which loops through the data to sort into largest to smallest
    if x==0: #Checks the number of items in list, if only 1 returns that integer
        return data[x] #returns the position of each integer
    v1 = data[x] #placeholder for current position of integer in list
    v2 = finder_rec(data, x-1)#placeholder for next integer in list, line 6 and 7 sort the data by position
    if v1>v2: #compares each integer in list to one another 
        return v1 #returns v1 if v1>v2
    else:
        return v2 #returns v2 if v2>v1, v2 is the position for the largest integer during each recursion
print (finder([0, -247, 341, 1001, 741, 22]))