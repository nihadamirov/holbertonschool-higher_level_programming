#!/usr/bin/python3
"""
Takes in a URL and email, sends a POST request with email as parameter
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare POST data
    data = urllib.parse.urlencode({'email': email}).encode('ascii')

    # Create request with required header to bypass firewall
    req = urllib.request.Request(url, data)
    req.add_header('cfclearance', 'true')

    # Send POST request and get response
    with urllib.request.urlopen(req) as response:
        # Read and decode response body
        body = response.read().decode('utf-8')
        print(body)