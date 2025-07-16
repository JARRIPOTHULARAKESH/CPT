'''a = int(input("Enter a marks: "))
b = int(input("Enter b marks: "))
c = int(input("Enter c marks: "))
count = 0
if a >= 35:
    count += 1
elif b >= 35:
    count += 1
elif c >= 35:
    count += 1
print("Number of subjects passed:", count)

a = [-1,3,0,3,-2]
negative_count = 0
positive_count = 0
for i in a:
    if i < 0:
        negative_count += 1
    elif i >= 0:
        positive_count += 1
print("Negative count:", negative_count)
print("Positive count:", positive_count)
for i in range(65,92):
    for j in range(0,11):
        spaces = " " * (10 - j)
        print(spaces + chr(i) + str(j))
    print()
    '''

'''rows = 5
for i in range(1, rows + 1):
    print('  ' * (rows - i), end='')

    for num in range(i, 0, -1):
        print(num, end=' ')

    for ch in range(65 + i - 1, 64, -1): 
        print(chr(ch), end=' ')
    
    print()'''




# a=[]
# sum=0
# for i in range(11):
#     a.append(i)
#     sum+=i
# print("Sum of first 10 natural numbers:", sum)


# a=[]
# n=int(input())
# for i in range(n):
#     a.append(i)
# for i in range(3):
#     print(max(a))
#     print(min(a))
#     a.remove(max(a))
#     a.remove(min(a))10


# a=[]
# n=int(input("Enter the number of elements: "))
# for i in range(n):
#     a.append(i)
# # b=print(a)
# c=a[::-1]
# print(c)


# from collections import Counter
# students=int(input())

# marks = []
# for i in range(students):
#     mark = int(input(f"Enter marks for student {i}: "))
#     marks.append(mark)
# print(Counter(marks))

# students=int(input())
# ten=0
# b=0
# c=0     
# d=0
# e=0 
# f=0
# g=0
# h=0
# k=0 
# j=0     

# marks = []
# for i in range(students):
#     mark = int(input(f"Enter marks for student {i}: "))
#     marks.append(mark)
# for i in marks:
#     if i>=0 and i<=10:
#         ten+=1
#     if i>=11 and i<=20:
#         b+=1
#     if i>=21 and i<=30:
#         c+=1
#     if i>=31 and i<=40:
#         d+=1
#     if i>=41 and i<=50:
#         e+=1    
#     if i>=51 and i<=60:
#         f+=1
#     if i>=61 and i<=70:
#         g+=1        
#     if i>=71 and i<=80:
#         h+=1  
#     if i>=81 and i<=90:
#         k+=1
#     if i>=91 and i<=100:
#         j+=1    
# print("Marks in range 0-10:", ten)
# print("Marks in range 11-20:", b)   
# print("Marks in range 21-30:", c) 
# print("Marks in range 31-40:", d)
# print("Marks in range 41-50:", e)           
# print("Marks in range 51-60:", f)
# print("Marks in range 61-70:", g)       
# print("Marks in range 71-80:", h)
# print("Marks in range 81-90:", k)   
# print("Marks in range 91-100:", j)


# str=input()
# c=str[::-1]
# print("Reversed string:", c)



# str = input("Enter a string: ").lower()
# s=str
# if 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s:
        
#     s=s.replace("a","z")
#     s=s.replace("e","z")
#     s=s.replace("i","z")
#     s=s.replace("o","z")
#     s=s.replace("u","z")
#     print(s)
# else:
#     print(str)



# str1 = input("Enter a string: ")
# str2 = input("Enter another string: ")  
# str3=str1 + str2
# print("Concatenated string:", str3)



# from collections import Counter
# str = input("Enter a string: ")
# c= Counter(str)
# print("Character count:", c)


# str1 = input("Enter a string: ")
# str2 = input("Enter another string: ")
# str2= str2[::-1]
# c= str1 + str2
# print("Concatenated string with second reversed:", c)



# arr1=eval(input("Enter first array: "))
# arr2=eval(input("Enter second array: "))
# arr3 = list(set(arr1 + arr2))
# arr3.sort()
# print("Merged and sorted array:", arr3)


# arr=eval(input("Enter an array: "))
# arr.sort()
# print("Sorted array:", arr[::-1])  

# arr=eval(input("Enter an array: "))

# c= list(set(arr))  # Remove duplicates
# c.sort()  # Sort the unique elements
# print("Unique elements in sorted order:", list(c))

# arr=eval(input("Enter an array: "))
# a=int(input())
# if a in arr:
#     print("Element found at index:", arr.index(a))  

# arr1=eval(input("Enter first array: "))
# arr2=eval(input("Enter second array: "))    
# arr1.sort()
# arr2.sort() 
# ma=arr1+arr2
# ma.sort()
# # print("Merged and sorted array:", ma)   
# # ma[::-1]  # Reverse the sorted array
# print("Reversed sorted array:", ma[::-1])
a=[int(i) for i in input().split()]
print(a)