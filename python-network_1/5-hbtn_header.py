#!/usr/bin/python3
"""
Takes in a URL, sends a request and displays the value of X-Request-Id header
"""

if __name__ == "__main__":
    import requests
    import sys

    # Get URL from command line argument
    url = sys.argv[1]

    # Headers to bypass firewall
    headers = {'cfclearance': 'true'}

    # Send GET request
    response = requests.get(url, headers=headers)

    # Get and print the X-Request-Id header value
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)