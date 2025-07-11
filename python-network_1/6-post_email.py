#!/usr/bin/python3
"""
Takes in a URL and email, sends a POST request with email as parameter
"""

if __name__ == "__main__":
    import requests
    import sys

    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Headers to bypass firewall
    headers = {'cfclearance': 'true'}

    # Data to send in POST request
    data = {'email': email}

    # Send POST request
    response = requests.post(url, data=data, headers=headers)

    # Display response body
    print(response.text)