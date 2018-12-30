import datetime
today = datetime.datetime.today()

dayofweek = today.weekday()

if dayofweek == 1:
    print("Its Tuesday")
else:
    print("Unfortuanately its not Tuesday")