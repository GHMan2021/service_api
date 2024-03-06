import requests


class ServiceTestApi:
    URL: str = "http://localhost:8080/api"
    POST_CREATE_ENTITY: str = "/create"
    DELETE_ENTITY: str = "/delete"
    GET_ENTITY: str = "/get"
    GET_ALL_ENTITIES: str = "/getAll"
    PATCH_UPDATE_ENTITY: str = "/patch"

    def create_entity(self, payload):
        return requests.post(f"{self.URL}{self.POST_CREATE_ENTITY}", json=payload)

    def delete_entity_by_id(self, obj_id):
        return requests.delete(f"{self.URL}{self.DELETE_ENTITY}/{obj_id}")

    def get_entity_by_id(self, obj_id):
        return requests.get(f"{self.URL}{self.GET_ENTITY}/{obj_id}")

    def get_all_entities(self):
        return requests.get(f"{self.URL}{self.GET_ALL_ENTITIES}")

    def update_entity_by_id(self, obj_id, payload):
        return requests.patch(f"{self.URL}{self.PATCH_UPDATE_ENTITY}/{obj_id}", json=payload)
