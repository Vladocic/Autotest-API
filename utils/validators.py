from pydantic import ValidationError

def validate_response_schema(data:dict, schema_class):
    try:
        return schema_class(**data)
    except ValidationError as e:
        raise AssertionError(f"Ошибка валидации Pydantic-схемы:\n{e}")
