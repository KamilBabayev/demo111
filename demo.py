#!/usr/bin/python3

import requests

url = 'http://api.ipify.org'

params = {'format': 'json'}

req = requests.get(url, params=params)

print(req.json())
print(req.json()['ip'])
