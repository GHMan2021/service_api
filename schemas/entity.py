from typing import List

from pydantic import BaseModel


class Addition(BaseModel):
    """Модель для дополнительной информации сущности."""

    additional_info: str
    additional_number: int
    id: int


class Entity(BaseModel):
    """Модель для сущности."""

    id: int
    important_numbers: List[int]
    title: str
    verified: bool
    addition: Addition
