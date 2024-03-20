from typing import Generator, List
import pytest
import requests

from generators.entity import EntityGenerator
from lib.module.service_test_api import ServiceTestApi


@pytest.fixture()
def create_object() -> requests.Response:
    """Фикстура для создания объекта.

    Генерирует случайный объект с использованием EntityGenerator,
    создает его через ServiceTestApi и возвращает ответ запроса.

    Returns:
    ----------
    requests.Response
        Ответ запроса на создание объекта.
    """
    payload = EntityGenerator.random()
    service = ServiceTestApi()
    response = service.create_entity(payload)
    return response


@pytest.fixture()
def delete_object() -> Generator[List[int], None, None]:
    """Фикстура для удаления объекта.

    Создает список идентификаторов объектов, которые должны быть удалены.
    Возвращает этот список и после завершения теста удаляет каждый объект из списка.

    Returns:
    ----------
    Generator[List[int], None, None]
        Генератор списка идентификаторов объектов для удаления.
    """
    obj_ids = []
    yield obj_ids
    for obj_id in obj_ids:
        service = ServiceTestApi()
        service.delete_entity_by_id(obj_id)
