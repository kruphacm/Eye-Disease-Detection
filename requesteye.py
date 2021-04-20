import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Enter the Symptom 1':0, 'Enter the Symptom 2':1, 'Enter the Symptom 3':2})

print(r.json())
