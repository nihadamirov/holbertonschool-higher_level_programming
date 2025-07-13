#!/usr/bin/python3
"""Sends request and handles HTTPError using urllib"""
import urllib.request
import urllib.error
import sys

url = sys.argv[1]

req = urllib.request.Request(url)

try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
