import json
name=input("enter the name:")
age=int(input("enter age:"))

user={"name":name,"age":age}

with open("user.json",'w') as f:
    json.dump(user,f)

print("Data written to json folder")

with open("user.json",'r') as f:
    loaded=json.load(f)
    print("Read from file",loaded)