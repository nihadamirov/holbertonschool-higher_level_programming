#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using urllib"""
import urllib.request

url = 'https://intranet.hbtn.io/status'
headers = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
