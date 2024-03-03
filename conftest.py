import pytest

from genetators.entity import EntityGenerator
from lib.module.service_test_api import ServiceTestApi


@pytest.fixture()
def create_object():
    payload = EntityGenerator.random()
    service = ServiceTestApi()
    res = service.create_entity(payload)
    return res


@pytest.fixture()
def delete_object():
    obj_ids = []
    yield obj_ids
    for obj_id in obj_ids:
        service = ServiceTestApi()
        service.delete_entity_by_id(obj_id)
