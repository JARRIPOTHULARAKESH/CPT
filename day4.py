#multiple inheritance
'''class base1(object):  #base class
    def __init__(self):
        super(base1,self).__init__()
        print("Base Class-1")
class base2(object):   #2nd base class
    def __init__(self):
        super(base2,self).__init__()
        print("Base class2")
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("derived class from both classes")
d=derived()'''
class addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)
class multiplication:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a*self.b)
class calc(addition,multiplication):
    def __init__(self,a,b):
        addition.__init__(self,a,b)
        multiplication.__init__(self,a,b)
        print("calc class initialized")
x=int(input("enter the 1st value:"))
y=int(input("enter 2nd value:"))
c=calc(x,y)
