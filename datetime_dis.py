import datetime
print(dir(datetime))

tday=datetime.date(2022,4,13)
# print("Year:",tday.year)
# print("Month:",tday.month)
# print("Day:",tday.day)

# print("Today:",datetime.date.today())
# ctime=datetime.datetime.now()
# print("System time:",ctime)  #mm/dd/yyyy hh:mm
# print(ctime.strftime("%m/%d/%Y %H:%M"))
# print(ctime.strftime("%A,%d %B, %Y  %I:%M:%S %p"))

tday=datetime.date.today()
dt=datetime.timedelta(100)
print(tday+dt)