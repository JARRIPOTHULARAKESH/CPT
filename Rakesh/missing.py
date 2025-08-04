import pandas as pd
import numpy as np
series=pd.Series([10,np.nan,30,np.nan,50],index=['a','b','c','d','e'])
print("Original Series:")
print(series)
print("missing values in the series:", series.isnull())