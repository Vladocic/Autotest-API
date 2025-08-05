from data.faker_instance import fake


def string_with_length(data:str, length:int) -> str:
    if len(data) < length:
        diff = length - len(data)
        data += fake.lexify("x" * diff)

    elif len(data) > length:
        data = data[:length]

    return data


def string_number_with_length(data:str, length:int = 30) -> str:
    digits_str = str(fake.random_number(digits=1))
    base_max_len = length - len(digits_str)
    data = data[:base_max_len] if len(data) >= base_max_len else "" 
    return data + digits_str

 

def generate_nonexistent_project_id(ids:list[int]) -> int:
    while True:
        uniq_id = fake.random_int(min=1, max=1000)
        if uniq_id not in ids:
            return uniq_id



def get_project_ids(response) -> list[int]:
    return [project["id"] for project in response["_embedded"]["elements"]]

