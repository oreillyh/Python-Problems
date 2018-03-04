#Iris Data sorted into columns
#Hugh O'Reilly 04/03/18
with open("data/iris.csv") as f: #Opens Iris data set csv file in data folder
    for line in f:# loops through each line
        line = line.replace(',', '  ') #replaces comma with space, code from Mohamed Noor
        line = line.rstrip() #Removes nextline code on end,  code from Mohamed Noor
        print(line.split(',')[:]) #Splits and Prints 
        #each line as a list, colon separates each item in
        # columns
    
                  




