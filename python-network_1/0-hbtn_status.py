#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib package
"""

if __name__ == "__main__":
    import urllib.request

    # URL to fetch
    url = "https://intranet.hbtn.io/status"

    # Create request with required header to bypass firewall
    req = urllib.request.Request(url)
    req.add_header('cfclearance', 'true')

    # Fetch the URL using with statement
    with urllib.request.urlopen(req) as response:
        body = response.read()

        # Display response body information
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))