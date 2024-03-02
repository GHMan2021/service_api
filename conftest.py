import pytest

from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject

from genetators.entity import EntityGenerator


@pytest.fixture()
def obj_id():
    create_object = CreateObject()
    payload = EntityGenerator.random()
    create_object.create_entity(payload)
    yield create_object.response_txt
    delete_object = DeleteObject()
    delete_object.delete_entity_by_id(create_object.response_txt)
