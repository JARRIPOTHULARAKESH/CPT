with open ("File1.txt",'a+')as file:
    file.write('\n Appended data')
    file.seek(0)
    print(file.read())