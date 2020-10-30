import requests

url = 'http://localhost:5000/api'
r = requests.post(url,json={'Monday':50, 'Tuesday':80})

print(r.json())