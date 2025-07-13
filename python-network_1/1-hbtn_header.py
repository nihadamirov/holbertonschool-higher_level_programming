#!/usr/bin/python3
"""Displays the X-Request-Id header using urllib"""
import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.headers
    print(headers.get('X-Request-Id'))
