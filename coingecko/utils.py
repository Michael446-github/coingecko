"""
Services, utilities, helpers for API
"""
from typing import Any

import requests


class Helper:
    @staticmethod
    def __check_bools(params: dict[str, Any]):
        """
        Convert 'True' to 'true' and 'False' to 'false'
        :param params: dictionary of parameters
        :return: converted parameters
        """

        for key, val in params.items():
            if type(val) == bool:
                params[key] = str(val).lower()

        return params

    def parse_params(self, params: dict[str, Any]):
        """
        Generate a string of parameters to add to url
        :param params: dictionary of GET parameters
        :return: '?param=value&param2=valu2' like string
        """

        if not params:
            return ""

        params = self.__check_bools(params)
        str_params = "&".join([f"{key}={val}" for key, val in params.items()])

        return f"?{str_params}"


class ApiClient:
    def __init__(self, base_url: str):
        self.BASE_URL = base_url
        self.helper = Helper()

    def get(self, route: str, **params) -> dict:
        url = f"{self.BASE_URL}{route}{self.helper.parse_params(params)}"
        res = requests.get(url)

        return res.json()
