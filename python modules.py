'''import random
num=[1,2,3,4,5]
random.seed(20)
print(random.randint(1,100))'''

#datetime

'''from datetime import datetime,date,timedelta
now=datetime.now()
print("Current datetime:",now)
print("Todays date:",date.today())
#formatted datetime

formatted=now.strftime("%d-%m-%Y %H:%M:%S")#string format time
print("Formatted datetime:",formatted)

#parsed datetime-converting to one datatype to another datatype

date_str="24-12-2000 14:55:00"
parsed=datetime.strptime(date_str,"%d-%m-%Y %H:%M:%S")#string parsed time
print("Parsed data:",parsed)

#timedelta

tommorow=now+timedelta(days=1)
print("Tommorow:",tommorow)
yesterday=now-timedelta(days=1)
print("yesteray:",yesterday)
ftime=now+timedelta(hours=3,minutes=35)
print("Ftime:",ftime)



now=datetime.now()
format_12hr=now.strftime("%d/%m/%Y %I:%M:%S %p")#%P : WORKS FOR BOTH AM AND PM %I=0-12
print(format_12hr)'''


#JSON MODULE

import json
name=input("enter your name:")
age=int(input("enter your age:"))
data={"name":name,"age":age}
stringify_json=json.dumps(data)
print("Serialised data of JSON",stringify_json)