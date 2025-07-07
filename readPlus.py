with open('File1.txt','r+')as file:
    n=file.read()
    file.seek(0)
    file.write("Modification done here ")