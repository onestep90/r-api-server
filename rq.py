#!/usr/bin/python3
import requests
URL = 'http://localhost:8000/sum?a=1&b=2'
response = requests.post(URL)
response.status_code
print(response.text)
