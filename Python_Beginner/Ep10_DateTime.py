import datetime as dt

today = dt.datetime.now()
print(today.day)
print(today.month)
print(today.year)

#format date
print(today.strftime("%x")) # 07/28/22 mm/dd/yy
print(today.strftime("%d-%m-%y")) # 28-07-22 dd/mm/yy
print(today.strftime("%c")) # Thu Jul 28 14:29:46 2022
print(today.strftime("%Y-%m-%d %H:%M:%S"))  # 2022-07-28 14:30:40
print(today.strftime("%H:%M:%S"))  # 14:31:03
print(today.strftime("%A,%d %B, %Y"))  # Thursday,28 July, 2022
print(today.strftime("%a,%d %b, %Y"))  # Thu,28 Jul, 2022
print(today.strftime("%d-%B-%Y"))  # T28-July-2022