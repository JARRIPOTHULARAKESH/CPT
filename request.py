import requests
response=requests.get("https://jsonplaceholder.typicode.com/post/1")
print("Status code:",response.status_code)
print("response JSON",response.json())