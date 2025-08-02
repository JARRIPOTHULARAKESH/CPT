'''import numpy as np
a=list(map(int,input("enter 3 numbers for array a, space separated: ").split()))
b=list(map(int,input("enter 3 numbers for array b, space separated: ").split()))
a=np.array(a)
b=np.array(b)
print("vertical stack:\n", np.vstack((a, b)))
print("horizontal stack:\n", np.hstack((a, b)))
import numpy as np
data=input("Enter a list of numbers separated by spaces: ")
arr=np.array(list(map(int, data.split())))
odd_nums=arr[arr%2==1]
print("Odd numbers in the array:", odd_nums)


#replacing NAN
import numpy as np
arr=np.array([1,np.nan,3,4,5])
print("replace Nan with 0:",np.where(np.isnan(arr), 0,arr))'''

import numpy as np
arr=np.array([1.5,2.9,9.8])
print(arr.astype(np.int32))
arr=np.array([1,2,3,4])
print(arr.astype(np.float64))
arr=np.array([1.5,2.9,9.8])
print(arr.astype(str))
arr=np.array([0,1,7,0])
print(arr.astype(bool))
arr=np.array([True,True,False,True])
print(arr.astype(np.int32))
arr=np.array([1.5,2.9,9.8])
print(arr.astype(np.complex128))

