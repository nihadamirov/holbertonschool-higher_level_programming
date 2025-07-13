#!/usr/bin/python3
"""Displays the X-Request-Id header using requests"""
import requests
import sys

url = sys.argv[1]
response = requests.get(url)
print(response.headers.get('X-Request-Id'))
