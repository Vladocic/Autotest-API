from pydantic import BaseModel, Field
from typing import Optional



class Project(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., description="Название проекта")
    identifier: str = Field(..., description="Уникальный идентификатор проекта")
    description: Optional[str] = Field(None, description="Описание проекта")

    class Config:
        extra = "ignore"