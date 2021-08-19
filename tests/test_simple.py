import unittest

from coingecko.simple import Simple


class TestSimple(unittest.TestCase):
    def setUp(self) -> None:
        self.simple = Simple()

    def tearDown(self) -> None:
        del self.simple

    def test_price_correct(self):
        res = self.simple.price("dogecoin", "usd")

        self.assertTrue("dogecoin" in res.keys())

    def test_price_with_incorrect_data(self):
        res = self.simple.price("gecoin", "usd")

        self.assertFalse(res)

    def test_price_with_params(self):
        res = self.simple.price("dogecoin", "usd", include_market_cap=True)

        self.assertTrue("usd_market_cap" in res["dogecoin"])

    def test_supported_vs_currencies(self):
        res = self.simple.supported_vs_currencies()

        self.assertTrue("btc" in res)
        self.assertTrue("usd" in res)
        self.assertTrue("gbp" in res)


if __name__ == '__main__':
    unittest.main()
