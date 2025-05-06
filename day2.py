#class and Object
'''class abc():
    var=100
    def display(self):
        print("This is a class method")
obj=abc()
print(obj.var)
obj.display()'''
#class constructor__init__(method)
'''class abc():
    def __init__(self,val):
        print("this is class method")
        self.val=val
        print("the value is:",val)
obj=abc(10)'''
#class obj variables
'''class abc():
    cv=0
    def __init__(self,var):
        abc.cv+=1
        self.var=var
        print("object var:",var)
        print("class var:",abc.cv)
obj=abc(10)
obj=abc(20)
obj=abc(30)'''
#code to illustrate the modification of an instance variable to check whether the passing attribute is even or odd,by creating a class number and function to check even or odd
'''class abc():
    even=0
    def check(self,val):
        if val%2==0:
            self.even=1
    def eo(self,val):
        self.check(val)
        if self.even==1:
            print("Given val is even")
        else:
            print("Given val is odd")
    

obj=abc()
val=int(input("enter the number:"))
obj.eo(val)'''
#segregrate the even and odd parameters in a list and print even list and odd list seperately using a class "number"
'''class number:
    odd=[]
    even=[]
    def __init__(self,num):
        if num%2==0:
            number.even.append(num)
        else:
            number.odd.append(num)

n1=number(21)
n2=number(32)
n3=number(43)
n4=number(54)
n5=number(65)
print(number.even)
print(number.odd)'''
#class methods
'''class abc:
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var-obj.var
obj=abc("abcdef",10)
print("the value stored in object is:",repr(obj))
print("the lenght of name stored in object:",len(obj))
obj1=abc("ghjijl",1)
val=obj.__cmp__(obj1)
if val==0:
    print("both vallues ar equal")
elif val==-1:
    print("1st value is less than second")
else:
    print("2nd value is less than first")'''

#Advanced control methods
'''
1.__call__()--instance can be directly called
2.__it__(),__le__(),__gt__(),__ge__(),__eq__(),__ne__()
3.__hash__()--decide obj/set/dict
4.__iter__()
5.__getitem__(),__setitem__()
'''
class numbers:
    def __init__(self,myself):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist=numbers([1,2,3,4,5,6,7,8,9])
print(numlist)
numlist[3]=10
print(numlist.mylist)
