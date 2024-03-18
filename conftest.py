from typing import Generator, List
import pytest
import requests

from generators.entity import EntityGenerator
from lib.module.service_test_api import ServiceTestApi


@pytest.fixture()
def create_object() -> requests.Response:
    payload = EntityGenerator.random()
    service = ServiceTestApi()
    response = service.create_entity(payload)
    return response


@pytest.fixture()
def delete_object() -> Generator[List[int], None, None]:
    obj_ids = []
    yield obj_ids
    for obj_id in obj_ids:
        service = ServiceTestApi()
        service.delete_entity_by_id(obj_id)
