import datetime
todayWithTime = datetime.datetime.today()
todayWithourTime = datetime.date.today()
print(todayWithTime)
print(todayWithourTime)
print("The current date is", datetime.datetime.strftime(todayWithourTime, "%m/%d/%Y"))
print("The current time is", datetime.datetime.strftime(todayWithTime, "%H:%M:%S"))
