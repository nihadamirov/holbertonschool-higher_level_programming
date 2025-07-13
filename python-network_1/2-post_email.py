#!/usr/bin/python3
"""Sends a POST request with an email using urllib"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')
req = urllib.request.Request(url, data=data)

with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
