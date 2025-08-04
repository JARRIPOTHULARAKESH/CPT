import pandas as pd
print("enter 4 random numbers separated with space:")
numbers=input().strip().split()
numbers=[float(num)for num in numbers]
try:
    if len(numbers)!=4:
        raise ValueError("please provide exactly 4 numbers")
    series=pd.Series(data=numbers)
    print(series)
    filtered=series[series>10]
    print(filtered)
except ValueError as e:
    print(e)
