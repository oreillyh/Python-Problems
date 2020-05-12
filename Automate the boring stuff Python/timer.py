import datetime

currentDate = datetime.date.today()

strDueDate = input("enter a due date for the project in mm/dd/yyyy format\n")
dueDate = datetime.datetime.strptime(strDueDate, "%m/%d/%Y").date()

daysLeft = dueDate - currentDate

print(f"You have {daysLeft} days left to finish your project.")