import pytest
import requests
from config.config import config
from data.projects_data import ProjectData
from data.users_data import UserData
from data.work_packages_data import WorkPackagesData


@pytest.fixture(scope="session")
def auth_headers() -> dict:
    return config.get_auth_headers()


@pytest.fixture
def api_session(auth_headers) -> requests.Session:
    session = requests.Session()
    session.headers.update(auth_headers)
    return session


@pytest.fixture
def created_project(api_session) -> int:
    project_data = ProjectData.valid()
    response = api_session.post(
        f"{config.api_base_url}/projects",
        json=project_data
    )
    assert response.status_code == 201
    return response.json()["id"]


@pytest.fixture
def created_user(api_session, user_data) -> requests.Response:
    response = api_session.post(
        f"{config.api_base_url}/users",
        json=user_data
    )
    assert response.status_code == 201
    return response


@pytest.fixture
def user_data(request):
    param = request.param

    if isinstance(param, dict) and "field" in param and "length" in param:
        field = param["field"]
        length = param["length"]

        if field == "login":
            return UserData.login_with_length(length)
        elif field == "firstName":
            return UserData.first_name_with_length(length)
        elif field == "lastName":
            return UserData.last_name_with_length(length)
        else:
            raise ValueError(f"Неизвестное поле: {field}")

    elif isinstance(param, dict):
        data = UserData.valid()
        data.update(param)
        return data

    elif callable(param):
        return param()

    raise ValueError("Некорректный формат user_data")


@pytest.fixture
def created_work_package(api_session, created_project) -> dict:
    work_data = WorkPackagesData(created_project).valid()
    response = api_session.post(
        f"{config.api_base_url}/projects/{created_project}/work_packages",
        json=work_data
    )
    assert response.status_code == 201
    return {
        "request": work_data,
        "response": response
    }

@pytest.fixture
def existing_project_ids(api_session) -> list[int]:
    response = api_session.get(f"{config.api_base_url}/projects")
    assert response.status_code == 200
    return [project["id"] for project in response.json()["_embedded"]["elements"]]
