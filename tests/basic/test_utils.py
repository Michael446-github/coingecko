import os
import unittest

from coingecko.utils import ApiClient

os.environ["BASE_URL"] = "https://api.coingecko.com/api/v3"


class TestUtils(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ApiClient(os.environ["BASE_URL"])

    def tearDown(self) -> None:
        del self.client

    def test_helper_parse_params(self):
        str_params = self.client.helper.parse_params({"param1": "value1", "param2": "value2"})

        self.assertEqual("?param1=value1&param2=value2", str_params)

    def test_api_client(self):
        res = self.client.get("/ping")

        self.assertEqual("(V3) To the Moon!", res["gecko_says"])


if __name__ == '__main__':
    unittest.main()
