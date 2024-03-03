import pytest

from genetators.entity import EntityGenerator
from lib.module.service_test_api import ServiceTestApi


@pytest.fixture()
def create_object():
    payload = EntityGenerator.random()
    service = ServiceTestApi()
    res = service.create_entity(payload)
    return res


def delete_object_by_id(obj_id):
    service = ServiceTestApi()
    service.delete_entity_by_id(obj_id)


@pytest.fixture()
def delete_object():
    yield delete_object_by_id