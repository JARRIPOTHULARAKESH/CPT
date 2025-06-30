'''import random
num=[1,2,3,4,5]
random.seed(20)
print(random.randint(1,100))'''

#datetime

from datetime import datetime,date,timedelta
now=datetime.now()
print("Current datetime:",now)
print("Todays date:",date.today())
#formatted datetime

formatted=now.strftime("%d-%m-%Y %H:%M:%S")#string format time
print("Formatted datetime:",formatted)