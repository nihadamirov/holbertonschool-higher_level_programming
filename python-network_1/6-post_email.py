#!/usr/bin/python3
"""Sends a POST request with email using requests"""
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)
print(response.text)
