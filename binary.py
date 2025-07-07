data=b'this is batch A data'
with open("binary_file.bin",'wb')as file:
    file.write(data)