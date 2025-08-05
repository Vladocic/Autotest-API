from typing import Any
from data.faker_instance import fake
from utils.generators import generate_nonexistent_project_id, string_with_length

class WorkPackagesData:

    def __init__(self, project_id:int):
        self.project_id = project_id

    def valid(self) -> dict[str, Any]:
        return {
            "project_id": self.project_id, 
            "subject": f"Задача: {fake.sentence(nb_words=4)}",
            "description": fake.paragraph(nb_sentences=3),
        }
    
    @staticmethod
    def with_empty_subject(project_id:int) -> dict[str, Any]:
        data = WorkPackagesData(project_id).valid()
        data["subject"] = ''
        return data
    

    @staticmethod
    def with_subject_length(project_id:int, length: int) -> dict[str, Any]:
        data = WorkPackagesData(project_id).valid()
        data["subject"] = string_with_length(data=data["subject"],length=length)
        return data

        
    @staticmethod
    def with_wrong_id(existing_ids: list[int]) -> dict[str, Any]:
        wrong_id = generate_nonexistent_project_id(ids=existing_ids)
        data = WorkPackagesData(wrong_id).valid()
        return data

