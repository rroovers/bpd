import datetime
today = datetime.datetime.today()
print(today)
last_monday = today + datetime.timedelta(days=-today.weekday())
print(today.weekday())

print(last_monday.strftime('%Y%m%d'))

yesterday = datetime.date(2022,7,3)
print(yesterday)
yesterday_weekday = yesterday.weekday()
print(yesterday_weekday)
print(datetime.datetime.today().weekday())
print(datetime.date.weekday())