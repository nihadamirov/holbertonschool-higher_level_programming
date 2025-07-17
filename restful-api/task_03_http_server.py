#!/usr/bin/env python3
"""
Simple API using Python's http.server module
Demonstrates basic HTTP server functionality with JSON responses
"""

import http.server
import json
import socketserver
from urllib.parse import urlparse


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler that extends BaseHTTPRequestHandler
    to create a simple API with multiple endpoints
    """

    def do_GET(self):
        """
        Handle GET requests and route them to appropriate endpoints
        """
        # Parse the URL path
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        # Route requests to different endpoints
        if path == '/':
            self.handle_root()
        elif path == '/data':
            self.handle_data()
        elif path == '/status':
            self.handle_status()
        elif path == '/info':
            self.handle_info()
        else:
            self.handle_404()

    def handle_root(self):
        """
        Handle requests to the root endpoint (/)
        Returns a simple greeting message
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()

        message = "Hello, this is a simple API!"
        self.wfile.write(message.encode('utf-8'))

    def handle_data(self):
        """
        Handle requests to the /data endpoint
        Returns sample JSON data
        """
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        # Sample dataset as specified in requirements
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }

        # Convert dictionary to JSON string and send response
        json_response = json.dumps(data)
        self.wfile.write(json_response.encode('utf-8'))

    def handle_status(self):
        """
        Handle requests to the /status endpoint
        Returns API status information
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()

        message = "OK"
        self.wfile.write(message.encode('utf-8'))

    def handle_info(self):
        """
        Handle requests to the /info endpoint
        Returns API information in JSON format
        """
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        info = {
            "version": "1.0",
            "description": "A simple API built with http.server"
        }

        json_response = json.dumps(info)
        self.wfile.write(json_response.encode('utf-8'))

    def handle_404(self):
        """
        Handle requests to undefined endpoints
        Returns 404 Not Found status with appropriate message
        """
        self.send_response(404)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()

        message = "404 Not Found"
        self.wfile.write(message.encode('utf-8'))

    def log_message(self, format, *args):
        """
        Override log_message to provide cleaner console output
        """
        print(f"[{self.log_date_time_string()}] {format % args}")


def run_server(port=8000):
    """
    Start the HTTP server on the specified port
    """
    try:
        with socketserver.TCPServer(("", port), SimpleAPIHandler) as httpd:
            print(f"Server running on http://localhost:{port}")
            print("Available endpoints:")
            print("  GET /        - Root endpoint (greeting)")
            print("  GET /data    - Sample JSON data")
            print("  GET /status  - API status")
            print("  GET /info    - API information")
            print("\nPress Ctrl+C to stop the server")

            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except OSError as e:
        print(f"Error starting server: {e}")
        print(f"Port {port} might already be in use. Try a different port.")


if __name__ == "__main__":
    run_server(8000)
