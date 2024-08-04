import unittest

from fastapi.testclient import TestClient
from .main import app


class TestMain(unittest.TestCase):

    client = TestClient(app)

    def test_root_request(self):
        response = self.client.get("/")
        self.assertTrue(response.status_code == 200)
        self.assertEqual(response.json(), {"hello": "world", "this": "is a response"})


if __name__ == "__main__":
    unittest.main()
