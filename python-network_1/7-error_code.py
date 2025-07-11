#!/usr/bin/python3
"""
Takes in a URL, sends a request and displays the body of response
Handles HTTP errors and prints error codes for status >= 400
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

    # Check if status code is >= 400 (error)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        # Display response body for successful requests
        print(response.text)