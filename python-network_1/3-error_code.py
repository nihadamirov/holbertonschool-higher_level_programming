#!/usr/bin/python3
"""
Takes in a URL, sends a request and displays the body of response
Handles HTTPError exceptions and prints error codes
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    # Get URL from command line argument
    url = sys.argv[1]

    try:
        # Create request with required header to bypass firewall
        req = urllib.request.Request(url)
        req.add_header('cfclearance', 'true')

        # Send request and get response
        with urllib.request.urlopen(req) as response:
            # Read and decode response body
            body = response.read().decode('utf-8')
            print(body)

    except urllib.error.HTTPError as e:
        # Handle HTTP errors and print error code
        print("Error code: {}".format(e.code))