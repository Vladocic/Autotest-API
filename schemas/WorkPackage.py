from pydantic import BaseModel, Field
from typing import Optional

class WorkPackage(BaseModel):
    id: int = Field(..., gt=0)
    subject: str = Field(..., min_length=1, max_length=255, description="Тема рабочего пакета")
    type: str = Field(..., description="Тип рабочего пакета")
    description: Optional[str] = Field(None, description="Описание")
    
    class Config:
        extra = "ignore"