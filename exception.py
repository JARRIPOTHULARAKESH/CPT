'''num=int(input("enter the numerator:"))
deno=int(input("enter the denominator:"))
try:
    quo=num/deno
    print("Quotient:",quo)
except ZeroDivisionError:
    print("Denominator canr be zero")'''

#multiple exception
'''try:
    num=int(input("enter number:"))
    print(num*4)
except KeyboardInterrupt:
    print("Number should be entered")
except ValueError:
    print("please chec before you enter the data type")
print("bye")'''


'''try:
    num=int(input("enter number:"))
    print(num*4)
except (KeyboardInterrupt,ValueError,TypeError):
    print("number should be entererd......Program Terminated!")
print("TaTa")'''

try:
    file=open('File1.txt')
    str=file.readline()
    print(str)
except IOError:
    print("error occured during input tae...")
else:
    print("u succesed the data")

