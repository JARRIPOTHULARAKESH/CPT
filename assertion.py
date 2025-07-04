'''c=int(input("Enter temperature in c :"))
f=(c*9/5)+32
assert(f<=32),"Its Cold"
print("Fahrenheit:",f)'''

#write a program which infinityley prints natural numbers.Raise a StopIteration exception after displaying first 20 numbers to ex
def display(n):
    while True:
        try:
            n+=1
            if n==21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n,end=' ')
i=0
display(i)
            