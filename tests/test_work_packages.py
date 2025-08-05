import pytest
from data.work_packages_data import WorkPackagesData
from core.base_test import BaseTest


class TestWorkPackageCreate(BaseTest):

    @pytest.mark.valid
    def test_create_work_package_success(self, created_work_package):
        request_data = created_work_package["request"]
        response = created_work_package["response"]
        response_data = response.json()

        self.assert_field_equals(
            actual=response_data["subject"],
            expected=request_data["subject"],
            field_name="subject"
        )
        self.assert_field_not_none(response_data["id"], "id")

    @pytest.mark.valid
    @pytest.mark.parametrize("length", [1, 2, 254, 255])
    def test_subject_valid_length(self, created_project, api_session, length):
        data = WorkPackagesData(created_project).with_subject_length(length)
        response = api_session.post(
            f"{self.api_url}/projects/{created_project}/work_packages",
            json=data
        )
        self.assert_response_success(response, expected_status=201)

    @pytest.mark.invalid
    @pytest.mark.parametrize("length", [0, 256])
    def test_subject_invalid_length(self, created_project, api_session, length):
        data = WorkPackagesData(created_project).with_subject_length(length)
        response = api_session.post(
            f"{self.api_url}/projects/{created_project}/work_packages",
            json=data
        )
        self.assert_response_error(response, expected_status=422)

    @pytest.mark.invalid
    def test_create_work_package_with_empty_subject(self, created_project, api_session):
        data = WorkPackagesData(created_project).with_empty_subject()
        response = api_session.post(
            f"{self.api_url}/projects/{created_project}/work_packages",
            json=data
        )
        self.assert_response_error(response, expected_status=422)

    @pytest.mark.invalid
    def test_create_work_package_with_nonexistent_project_id(self, existing_project_ids, api_session):
        data = WorkPackagesData.with_wrong_id(existing_project_ids)
        wrong_id = data["project_id"]
        response = api_session.post(
            f"{self.api_url}/projects/{wrong_id}/work_packages",
            json=data
        )
        self.assert_response_error(response, expected_status=404)

    @pytest.mark.invalid
    def test_create_work_package_with_project_id_0(self, api_session):
        data = WorkPackagesData(0).valid()
        response = api_session.post(
            f"{self.api_url}/projects/0/work_packages",
            json=data
        )
        self.assert_response_error(response, expected_status=404)
