'''with open ('File1.txt',"r") as file:
    content=file.read()
    print(content)'''

with open ('File1.txt',"a") as file:
    file.write("Wipro,TCS,Capegemin\n")
    file.write("this is append data \n")
