import pandas as pd
# data={'Name':['Rakesh','Ravi','Raj','Rohan','Rahul'],
#         'Age':[25,30,22,28,26],
#         'Branch':['CSE','ECE','ME','CSE','IT']}
# df=pd.DataFrame(data)
# print(df)
name=list(map(str, input("enter the names:").strip().split()))
age=list(map(int, input("enter the ages:").strip().split()))
branch=list(map(str, input("enter the branches:").strip().split()))
d={'Name':name, 'Age':age, 'Branch':branch}
df=pd.DataFrame(d)
print(df)