from pydantic import BaseModel, Field, EmailStr, field_validator


class User(BaseModel):
  id: int = Field(..., gt=0)
  login: str = Field(..., max_length=256, description="Логин пользователя")
  firstName: str = Field(..., max_length=30, description="Имя") 
  lastName: str = Field(..., max_length=30, description="Фамилия")
  email: EmailStr = Field(..., max_length=60, description="Email пользователя")

  class Config:
    extra = "ignore"
    

  @field_validator("email")
  def max_email_length(cls, v):
    if len(v) > 60:
      raise ValueError("Длина email не должна быть более 60 символов")
    else:
      return v