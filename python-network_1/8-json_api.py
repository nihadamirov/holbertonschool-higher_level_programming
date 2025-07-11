#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to search_user API
Handles JSON responses and displays results appropriately
"""

if __name__ == "__main__":
    import requests
    import sys

    # Get letter from command line argument, or set to empty string
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    # URL for the search API
    url = "http://0.0.0.0:5000/search_user"

    # Data to send in POST request
    data = {'q': letter}

    # Send POST request
    response = requests.post(url, data=data)

    try:
        # Try to parse JSON response
        json_response = response.json()

        # Check if JSON is empty
        if not json_response:
            print("No result")
        else:
            # Display id and name from JSON response
            user_id = json_response.get('id')
            name = json_response.get('name')
            print("[{}] {}".format(user_id, name))

    except ValueError:
        # Handle invalid JSON
        print("Not a valid JSON")