import requests
from endpoints.base_endpoint import Endpoint


class DeleteObject(Endpoint):
    DELETE_ENTITY = "/delete"

    def delete_entity_by_id(self, obj_id):
        self.response = requests.delete(f"{self.URL}{self.DELETE_ENTITY}/{obj_id}")
