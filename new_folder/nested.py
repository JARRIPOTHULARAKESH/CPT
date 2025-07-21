#lambda functions
'''(a+b)*c expression lambda evaluate and returns to another lambda'''

#l2=lambda a: lambda b,c:(a+b)*c # This lambda takes one argument and returns another lambda
#l1=l2(3)
#value=l1(1,2)
# Output the result
#print(value)
o=(lambda a: lambda b,c:(a+b)*c)(5)(3,2)
print(o)  # This will print the result of the lambda expression)

'''o=(lambda a: lambda b: lambda c: lambda d:(a+b)*c*d)(2)(3)(4)(5)
print(o)  # This will print the result of the nested lambda expression


num=int(input("a:"))
n=int(input("x:"))
oper=lambda a:lambda x:(x+a)**2
numsq=oper(num) #5
print(numsq(n))  # This will print the square of (n + num)'''

try:
    o=(lambda a: lambda b: lambda c,d:(a-b)/(c-d)(10)(4)(8,8))
    print(o)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except typeError:
    print("Invalid input type. Please ensure all inputs are numbers.")