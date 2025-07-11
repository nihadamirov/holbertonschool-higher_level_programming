#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests package
"""

if __name__ == "__main__":
    import requests

    # URL to fetch
    url = "https://intranet.hbtn.io/status"

    # Headers to bypass firewall
    headers = {'cfclearance': 'true'}

    # Send GET request
    response = requests.get(url, headers=headers)

    # Display response body information
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))