from typing import Union, Type

from schemas.entity import Entity


def check_validate_response(data: Union[list, dict], schema: Type[Entity]) -> None:
    """Проверяет и валидирует данные с использованием схемы Entity.

    Attributes:
    ----------
    data : Union[list, dict]
        Данные, которые требуется проверить и валидировать. Могут быть представлены как списком (для коллекции данных)
        или словарем (для одиночной записи).
    schema : Type[Entity]
        Тип схемы Entity, используемый для валидации данных.
    """
    if isinstance(data, list):
        for item in data:
            schema.model_validate(item)
    else:
        schema.model_validate(data)
