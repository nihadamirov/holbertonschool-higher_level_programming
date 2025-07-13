#!/usr/bin/python3
"""Displays the value of the X-Request-Id header using urllib"""
import urllib.request
import sys

url = sys.argv[1]
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    print(response.headers.get('X-Request-Id'))
