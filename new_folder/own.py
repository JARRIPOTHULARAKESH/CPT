'''colors=['red', 'green', 'blue','yellow', 'orange']
print([color.upper() for color in colors ])'''

from calendar import *
year =int(input("Enter a year: "))
if isleap(year):
    print(year,"is leap year")
else:
    print(year,"year is not leap year")

'''from datetime import *
d=date.today()
print(d)
d=date(1966,6,29)
for x in range(1,10):
    nextdate=d+timedelta(days=x)
    print(nextdate)'''