from typing import Any
from data.faker_instance import fake

class ProjectData:
    
    @staticmethod
    def valid() -> dict[str, Any]:
        return {
            "name": f"Проект {fake.company}",
            "identifier": f"proj-{fake.unique.random_number(digits=6)}",
            "description": fake.text(max_nb_chars=200)
        }