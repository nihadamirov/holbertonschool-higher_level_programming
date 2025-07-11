#!/usr/bin/python3
"""
Takes GitHub credentials and uses GitHub API to display user id
Uses Basic Authentication with personal access token
"""

if __name__ == "__main__":
    import requests
    import sys

    # Get username and password (personal access token) from command line
    username = sys.argv[1]
    password = sys.argv[2]

    # GitHub API URL for user information
    url = "https://api.github.com/user"

    # Send GET request with Basic Authentication
    response = requests.get(url, auth=(username, password))

    # Check if authentication was successful
    if response.status_code == 200:
        # Parse JSON response and get user id
        user_data = response.json()
        user_id = user_data.get('id')
        print(user_id)
    else:
        # Print None for failed authentication
        print("None")