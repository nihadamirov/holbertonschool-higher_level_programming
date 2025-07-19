#!/usr/bin/python3
"""Sends a request and handles HTTPError with urllib"""
import urllib.request
import urllib.error
import sys

url = sys.argv[1]
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
