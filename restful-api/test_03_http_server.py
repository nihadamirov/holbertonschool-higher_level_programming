#!/usr/bin/env python3

import unittest
import json
import requests
import subprocess
import time

class TestSimpleAPI(unittest.TestCase):

    BASE_URL = "http://localhost:8000"

    @classmethod
    def setUpClass(cls):
        # Start the server in a subprocess
        cls.server_process = subprocess.Popen(['python3', 'task_03_http_server.py'])
        # Wait for the server to start
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # Terminate the server process
        cls.server_process.terminate()
        cls.server_process.wait()

    def test_root_endpoint(self):
        response = requests.get(self.BASE_URL + '/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, this is a simple API!")

    def test_data_endpoint(self):
        response = requests.get(self.BASE_URL + '/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        data = response.json()
        expected_data = {"name": "John", "age": 30, "city": "New York"}
        self.assertEqual(data, expected_data)

    def test_status_endpoint(self):
        response = requests.get(self.BASE_URL + '/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'text/plain')
        self.assertEqual(response.text, "OK")

    def test_404_endpoint(self):
        response = requests.get(self.BASE_URL + '/undefined')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers['Content-Type'], 'text/plain')
        self.assertEqual(response.text, "404 Not Found")

if __name__ == '__main__':
    unittest.main()