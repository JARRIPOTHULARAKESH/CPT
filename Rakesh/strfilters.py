import pandas as pd
print("enter 5 strings separated with space:")
strings=input().strip().split()
print("enter substring:")
substring=input().strip()
try:
    if len(strings) !=5:
        raise ValueError("please provide exactly 5 strings")
    series=pd.Series(data=strings)
    print("Original Series:")
    print(series)
    filtered=series[series.str.lower().str.contains(substring.lower(),na=False)]
    print("Filtered Series containing substring '{}':".format(substring))
except ValueError as e:
    print(e)

