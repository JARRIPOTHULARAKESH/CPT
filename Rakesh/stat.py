import pandas as pd
print("enter 5 randaom numbers separated with space:")
numbers=input().strip().split()
numbers=[float(num) for num in numbers]
try:
    if len(numbers) != 5:
        raise ValueError("please provide exactly 5 numbers")
    series=pd.Series(numbers,index=['a', 'b', 'c', 'd', 'e'])
    print("Original Series:")
    print(series)
    print("\n Statistics of the series:")
    print("Mean:", series.mean())
    print("Maximum:", series.max())
    print("Minimum:", series.min())
    print("Sum:", series.sum())
    print('\n Attributes of the series:')
    print("Index:", series.index.tolist())
    print("Values:", series.values.tolist())
    print("Data Type:", series.dtype)
except ValueError as e:
    print(e)
