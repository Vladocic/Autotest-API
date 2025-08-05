import pytest
from conftest import created_user
from core.base_test import BaseTest
from data.users_data import UserData


class TestUserCreate(BaseTest):

    @pytest.mark.valid
    @pytest.mark.parametrize("user_data", [UserData.valid()], indirect=True)
    def test_create_user_success(self, user_data, created_user):
        response = created_user
        response_dict = response.json()

        self.assert_field_equals(
            actual=response_dict["login"], expected=user_data["login"], field_name="login")
        self.assert_field_equals(
            actual=response_dict["firstName"], expected=user_data["firstName"], field_name="firstName")
        self.assert_field_equals(
            actual=response_dict["lastName"], expected=user_data["lastName"], field_name="lastName")
        self.assert_field_equals(
            actual=response_dict["email"], expected=user_data["email"], field_name="email")

    @pytest.mark.valid
    @pytest.mark.parametrize("user_data", [
        {"field": "login", "length": 1},
        {"field": "login", "length": 255},
        {"field": "login", "length": 256},
    ], indirect=True)
    def test_user_login_valid_length(self, user_data, created_user):
        response = created_user
        self.assert_response_success(response=response, expected_status=201)

    @pytest.mark.invalid
    @pytest.mark.parametrize("user_data", [
        {"field": "login", "length": 0},
        {"field": "login", "length": 257}
    ], indirect=True)
    def test_user_login_invalid_length(self, user_data, api_session):
        response = api_session.post(
            f"{self.api_url}/users",
            json=user_data
        )
        self.assert_response_error(response=response, expected_status=422)

    @pytest.mark.valid
    @pytest.mark.parametrize("user_data", [
        {"field": "firstName", "length": 1},
        {"field": "firstName", "length": 29},
        {"field": "firstName", "length": 30},
    ], indirect=True)
    def test_user_first_name_valid_length(self, user_data, created_user):
        response = created_user
        response_dict = response.json()
        self.assert_response_success(response, expected_status=201)
        self.assert_field_equals(
            response_dict["firstName"], user_data["firstName"], "firstName")

    @pytest.mark.invalid
    @pytest.mark.parametrize("user_data", [
        {"field": "firstName", "length": 0},
        {"field": "firstName", "length": 31},
    ], indirect=True)
    def test_user_first_name_invalid_length(self, user_data, api_session):
        response = api_session.post(
            f"{self.api_url}/users",
            json=user_data
        )
        print("📨 Payload:", user_data)
        self.assert_response_error(response, expected_status=422)

    @pytest.mark.valid
    @pytest.mark.parametrize("user_data", [
        {"field": "lastName", "length": 1},
        {"field": "lastName", "length": 29},
        {"field": "lastName", "length": 30},
    ], indirect=True)
    def test_user_last_name_valid_length(self, user_data, created_user):
        response = created_user
        response_dict = response.json()
        self.assert_response_success(response, expected_status=201)
        self.assert_field_equals(
            response_dict["lastName"], user_data["lastName"], "lastName")

    @pytest.mark.invalid
    @pytest.mark.parametrize("user_data", [
        {"field": "lastName", "length": 0},
        {"field": "lastName", "length": 31},
    ], indirect=True)
    def test_user_last_name_invalid_length(self, user_data, api_session):
        response = api_session.post(
            f"{self.api_url}/users",
            json=user_data
        )
        print("📨 Payload:", user_data)
        self.assert_response_error(response, expected_status=422)

    @pytest.mark.edgecase
    @pytest.mark.parametrize("user_data", [UserData.login_with_digits()], indirect=True)
    def test_create_user_login_only_digits(self, user_data, api_session):
        response = api_session.post(f"{self.api_url}/users", json=user_data)
        assert response.status_code in [201, 422], \
            f"Ожидали 201 или 422, получили: {response.status_code}. Ответ: {response.text}"

    @pytest.mark.edgecase
    @pytest.mark.parametrize("user_data", [UserData.first_name_with_digits()], indirect=True)
    def test_create_user_first_name_only_digits(self, user_data, api_session):
        response = api_session.post(f"{self.api_url}/users", json=user_data)
        assert response.status_code in [201, 422], \
            f"Ожидали 201 или 422, получили: {response.status_code}. Ответ: {response.text}"

    @pytest.mark.edgecase
    @pytest.mark.parametrize("user_data", [UserData.last_name_with_digits()], indirect=True)
    def test_create_user_last_name_only_digits(self, user_data, api_session):
        response = api_session.post(f"{self.api_url}/users", json=user_data)
        assert response.status_code in [201, 422], \
            f"Ожидали 201 или 422, получили: {response.status_code}. Ответ: {response.text}"

    @pytest.mark.invalid
    @pytest.mark.parametrize("user_data", [UserData.empty_email()], indirect=True)
    def test_create_user_empty_email(self, user_data, api_session):
        response = api_session.post(f"{self.api_url}/users", json=user_data)
        self.assert_response_error(response, expected_status=422)

    @pytest.mark.invalid
    @pytest.mark.parametrize("user_data", [
        {"email": "invalid@@mail.com"},
        {"email": "пользователь@почта.рф"},
        {"email": "noatsymbol.com"},
    ], indirect=True)
    def test_create_user_invalid_email(self, user_data, api_session):
        response = api_session.post(f"{self.api_url}/users", json=user_data)
        self.assert_response_error(response, expected_status=422)
