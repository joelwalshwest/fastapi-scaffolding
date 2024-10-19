import unittest

from fastapi.testclient import TestClient
from src import main


class TestDebug(unittest.TestCase):

    _CLIENT = TestClient(main.app)

    def test_health_check(self):
        response = self._CLIENT.get("/debug/health_check")

        self.assertTrue(response.status_code == 200)
        self.assertEqual(response.json(), "all systems go")


if __name__ == "__main__":
    unittest.main()
