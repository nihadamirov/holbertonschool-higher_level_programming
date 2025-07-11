#!/usr/bin/python3
"""
Takes in a URL, sends a request and displays the value of X-Request-Id header
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    # Get URL from command line argument
    url = sys.argv[1]

    # Create request with required header to bypass firewall
    req = urllib.request.Request(url)
    req.add_header('cfclearance', 'true')

    # Send request and get response
    with urllib.request.urlopen(req) as response:
        # Get the X-Request-Id header value
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)