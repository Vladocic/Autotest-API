from typing import Any
import requests
from config.config import config

class BaseTest:

    def setup_method(self):
        self.base_url = config.api_base_url
        self.api_url = config.api_base_url
        self.headers = config.get_auth_headers()


    def assert_response_success(self, response: requests.Response, expected_status: int = 200):
        assert response.status_code == expected_status, \
            f"Статус кода должен быть {expected_status}, получили {response.status_code}. Ответ: {response.text}"


    def assert_response_error(self, response: requests.Response, expected_status:int):
        assert response.status_code == expected_status, \
            f"Статус код должен быть {expected_status}, получили {response.status_code}"

        
    def assert_field_equals(self, actual: Any, expected: Any, field_name:str):
        assert actual == expected, \
            f"Поле '{field_name}' должно быть {expected}, получили: {actual}"
        

    def assert_field_not_none(self, value: Any, field_name: str):
        assert value is not None, f"Поле '{field_name}' не должно быть None"





