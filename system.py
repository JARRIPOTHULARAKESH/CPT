import sys
'''print("Script name:",sys.argv[0])
print("All args:",sys.argv[1:])
print("Number of items:",len(sys.argv))
print("Included file name:",sys.argv)
if len(sys.argv)>1:
    print("First arg:",sys.argv[1])
else:
    print("No arguments provided")'''

'''num1=int(sys.argv[1])
num2=int(sys.argv[2])
num3=int(sys.argv[3])
print("product:",num1*num2*num3)'''

if len(sys.argv) != 3:
    print("Usage:python sample.py l b")
else:
    l = int(sys.argv[1])
    b = int(sys.argv[2])
    area = l * b
    print("Area of rectangle:", area)
