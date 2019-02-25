def finder(data):
     return finder_rec(data, len(data)-1)
def finder_rec(data,x):
    if x==0:
        return data[x]
    v1 = data[x]
    v2 = finder_rec(data, x-1)
    if v1>v2:
        return v1
    else:
        return v2