from rest_framework.test import APIClient
from unittest import TestCase


class TestSampleView(TestCase):
    def test_response_ok(self):
        URL = "/api/v1/test/"
        client = APIClient()
        response = client.get(URL)
        self.assertEqual(response.status_code, 200)
