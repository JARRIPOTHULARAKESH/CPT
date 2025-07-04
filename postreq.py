import requests
url="https://jsonplaceholder.typicode.com/post"
data={
    "title":"Hi students",
    "body":"Wipro Geeks",
    "userId":1}
response=requests.post(url,json=data)
print("Status Code",response.status_code)
print("Response json",response.json())