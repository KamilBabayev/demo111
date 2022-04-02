#!/usr/bin/python3

import requests

url = 'http://api.ipify.org'

params = {'format': 'json'}

req = requests.get(url, pararms=params)

print(req.json())
