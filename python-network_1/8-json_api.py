#!/usr/bin/python3
"""Sends a POST request with a search letter"""
import requests
import sys

q = "" if len(sys.argv) == 1 else sys.argv[1]
url = "http://0.0.0.0:5000/search_user"
response = requests.post(url, data={'q': q})

try:
    json = response.json()
    if json:
        print("[{}] {}".format(json.get('id'), json.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
