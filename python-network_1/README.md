# Python - Network #1

This project focuses on learning how to fetch internet resources using Python's urllib and requests packages. The main goal is to understand HTTP requests, responses, and how to manipulate data from external services.

## Learning Objectives

By the end of this project, you should be able to explain:

- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests (which is simpler than urllib)
- How to make HTTP GET requests
- How to make HTTP POST/PUT/etc. requests
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Your code should use the `pycodestyle` style
- All files must be executable
- All modules should have documentation
- You must use `get` to access dictionary values by key
- Your code should not be executed when imported (use `if __name__ == "__main__":`)

### Firewall Bypass
The intranet is hosted behind a firewall. To allow your requests to bypass it, you need to add this specific header:
```python
'cfclearance': 'true'
```

## Files Description

### Task 0: What's my status? #0
**File:** `0-hbtn_status.py`
- Fetches `https://intranet.hbtn.io/status` using urllib package
- Displays response body type, content, and UTF-8 decoded content
- Uses `with` statement for proper resource management

### Task 1: Response header value #0
**File:** `1-hbtn_header.py`
- Takes a URL as command line argument
- Sends request and displays the value of `X-Request-Id` header
- Uses urllib and sys packages only

### Task 2: POST an email #0
**File:** `2-post_email.py`
- Takes URL and email as command line arguments
- Sends POST request with email as parameter
- Displays response body decoded in UTF-8
- Uses urllib and sys packages only

### Task 3: Error code #0
**File:** `3-error_code.py`
- Takes URL as command line argument
- Manages `urllib.error.HTTPError` exceptions
- Prints "Error code: " followed by HTTP status code for errors
- Uses urllib and sys packages only

### Task 4: What's my status? #1
**File:** `4-hbtn_status.py`
- Same as Task 0 but using requests package instead of urllib
- Simpler and cleaner code thanks to requests library

### Task 5: Response header value #1
**File:** `5-hbtn_header.py`
- Same as Task 1 but using requests package
- Takes URL and displays `X-Request-Id` header value

### Task 6: POST an email #1
**File:** `6-post_email.py`
- Same as Task 2 but using requests package
- Sends POST request with email parameter

### Task 7: Error code #1
**File:** `7-error_code.py`
- Same as Task 3 but using requests package
- Handles HTTP errors (status code >= 400)
- Prints error code or response body accordingly

### Task 8: Search API
**File:** `8-json_api.py`
- Takes a letter as command line argument (optional)
- Sends POST request to `http://0.0.0.0:5000/search_user`
- Handles JSON responses appropriately:
    - Valid JSON with data: displays `[<id>] <name>`
    - Valid but empty JSON: displays "No result"
    - Invalid JSON: displays "Not a valid JSON"

### Task 9: My GitHub!
**File:** `10-my_github.py`
- Takes GitHub username and personal access token as arguments
- Uses GitHub API with Basic Authentication
- Displays user ID or "None" if authentication fails
- Requires `read:user` permission on the personal access token

## Usage Examples

### Basic GET request
```bash
./0-hbtn_status.py
```

### GET request with header extraction
```bash
./1-hbtn_header.py https://intranet.hbtn.io
```

### POST request with data
```bash
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

### Error handling
```bash
./3-error_code.py http://0.0.0.0:5000/status_404
```

### JSON API interaction
```bash
./8-json_api.py a
```

### GitHub API with authentication
```bash
./10-my_github.py your_username your_personal_access_token
```

## Key Concepts Demonstrated

1. **urllib vs requests**: The project shows the difference between Python's built-in urllib and the third-party requests library
2. **HTTP Methods**: Implementation of GET and POST requests
3. **Error Handling**: Proper handling of HTTP errors and exceptions
4. **JSON Processing**: Parsing and validating JSON responses
5. **Authentication**: Basic HTTP authentication with APIs
6. **Header Manipulation**: Adding custom headers and extracting response headers

## Testing

All scripts can be tested using the provided web server running on port 5000. Make sure to test in the container environment as specified in the project requirements.

## Repository Information

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `python-network_1`
- **Files:** All Python scripts listed above