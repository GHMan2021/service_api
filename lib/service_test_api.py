from typing import Union, Type

from schemas.entity import Entity


def check_validate_response(data: Union[list, dict], schema: Type[Entity]) -> None:
    if isinstance(data, list):
        for item in data:
            schema.model_validate(item)
    else:
        schema.model_validate(data)
