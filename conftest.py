import pytest
import requests
from config.config import config
from data.projects_data import ProjectData
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
def created_work_package(api_session, created_project) -> dict:
    work_data = WorkPackagesData(created_project).valid()
    response = api_session.post(
        f"{config.api_base_url}/projects/{created_project}/work_packages",
        json=work_data
    )
    assert response.status_code == 201
    return response.json()


@pytest.fixture
def existing_project_ids(api_session) -> list[int]:
    response = api_session.get(f"{config.api_base_url}/projects")
    assert response.status_code == 200
    return [project["id"] for project in response["_embedded"]["elements"]]
