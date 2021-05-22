import datetime

print(dir(datetime))
help(datetime.date)

date1 = datetime.date(2021, 5, 22)
print(date1)  # 2021-05-22
print(date1.day)  # 22
print(date1.month)  # 5
print(date1.year)  # 2021

delta = datetime.timedelta(100)  # 100days
print(date1 + delta)  # 2021-08-30

print(date1.strftime("%A, %B %d, %Y"))  # Saturday, May 22, 2021

# %A - full name of the day # Saturday
# %B - full name of the month # May
# %d - day of the month # 22
# %Y - four digit year # 2021

message = "Today is {:%A, %B %d, %Y}"
print(message.format(date1))  # Today is Saturday, May 22, 2021

date2 = datetime.date(2021, 5, 23)
print(date2)  # 2021-05-23
time2 = datetime.time(20, 45, 59)
print(time2)  # 20:45:59
datetime2 = datetime.datetime(2021, 5, 23, 20, 45, 59)
print(datetime2)  # 2021-05-23 20:45:59

current_datetime = datetime.datetime.today()
print(current_datetime)  # 2021-05-22 11:09:31.903016
# help(datetime.datetime)
print(current_datetime.microsecond)  # 903016

holidays = "7/1/2021"

holidays_datetime = datetime.datetime.strptime(holidays, "%d/%m/%Y")
print(holidays_datetime)
print(type(holidays_datetime))  # <class 'datetime.datetime'>




