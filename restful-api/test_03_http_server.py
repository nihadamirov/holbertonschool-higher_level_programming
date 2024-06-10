#!/usr/bin/env python3

import unittest
import json
import requests

class TestSimpleAPI(unittest.TestCase):

    BASE_URL = "http://localhost:8000"

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
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        status = response.json()
        expected_status = {"status": "OK"}
        self.assertEqual(status, expected_status)

    def test_404_endpoint(self):
        response = requests.get(self.BASE_URL + '/undefined')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        error_message = response.json()
        expected_error_message = {"error": "Endpoint not found"}
        self.assertEqual(error_message, expected_error_message)