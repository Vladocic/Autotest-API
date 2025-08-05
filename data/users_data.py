from typing import Any
from data.faker_instance import fake
from utils.generators import string_number_with_length, string_with_length


class UserData:

    @staticmethod
    def valid() -> dict[str, Any]:
        return {
            "login": fake.unique.user_name(),
            "password": fake.password(),
            "firstName": fake.name(),
            "lastName": fake.last_name(),
            "email": fake.unique.email(),
            "admin": False,
            "status": "active",
            "language": "en"
        }

    @staticmethod
    def login_with_length(length: int) -> dict[str, Any]:
        data = UserData.valid()
        data["login"] = string_with_length(
            data=data["login"], length=length)
        return data

    @staticmethod
    def first_name_with_length(length: int) -> dict[str, Any]:
        data = UserData.valid()
        data["firstName"] = string_with_length(
            data=data["firstName"], length=length)
        return data

    @staticmethod
    def last_name_with_length(length: int) -> dict[str, Any]:
        data = UserData.valid()
        data["lastName"] = string_with_length(
            data=data["lastName"], length=length)
        return data

    @staticmethod
    def first_name_with_digits() -> dict[str, Any]:
        data = UserData.valid()
        data["firstName"] = fake.random_number()
        return data

    @staticmethod
    def last_name_with_digits() -> dict[str, Any]:
        data = UserData.valid()
        data["lastName"] = fake.random_number()
        return data

    @staticmethod
    def empty_email() -> dict[str, Any]:
        return UserData.valid() | {"email": ""}
