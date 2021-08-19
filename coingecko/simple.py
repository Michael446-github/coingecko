"""
This file provides basic api calls for coingeckos simple subcatalog.
"""
import os

from coingecko.utils import ApiClient

os.environ["BASE_URL"] = "https://api.coingecko.com/api/v3"


class Simple:
    def __init__(self):
        self.client = ApiClient(os.environ["BASE_URL"] + "/simple")

    def price(self, ids: str, vs_currencies: str, **params) -> dict[str, dict]:
        from_to = {"ids": ids, "vs_currencies": vs_currencies}
        params = {**from_to, **params}

        res = self.client.get("/price", **params)
        return res

    def supported_vs_currencies(self) -> dict:
        res = self.client.get("/supported_vs_currencies")
        return res
