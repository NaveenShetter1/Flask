import requests
url='http://127.0.0.1:5000/add_data'


name=input("Enter your name")
age=input("Enter your age")
city=input("Enter your city name")

data={'name':name,'age':age,'city':city}
response=requests.post(url,json=data)
print(response.json())