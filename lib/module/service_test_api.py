import requests


class ServiceTestApi:
    """Класс для взаимодействия с тестовым API сервиса.

    Attributes:
    ----------
    URL : str
        URL-адрес базового API сервиса.
    POST_CREATE_ENTITY : str
        Путь к эндпоинту для создания сущности.
    DELETE_ENTITY : str
        Путь к эндпоинту для удаления сущности по ID.
    GET_ENTITY : str
        Путь к эндпоинту для получения сущности по ID.
    GET_ALL_ENTITIES : str
        Путь к эндпоинту для получения всех сущностей.
    PATCH_UPDATE_ENTITY : str
        Путь к эндпоинту для обновления сущности по ID.
    """
    URL: str = "http://localhost:8080/api"
    POST_CREATE_ENTITY: str = "/create"
    DELETE_ENTITY: str = "/delete"
    GET_ENTITY: str = "/get"
    GET_ALL_ENTITIES: str = "/getAll"
    PATCH_UPDATE_ENTITY: str = "/patch"

    def create_entity(self, payload: dict) -> requests.Response:
        """Создает новую сущность с использованием API.

        Args:
        ----------
        payload : dict
            Словарь с данными для создания сущности.

        Returns:
        ----------
        requests.Response
            Объект ответа запроса.
        """
        return requests.post(f"{self.URL}{self.POST_CREATE_ENTITY}", json=payload)

    def delete_entity_by_id(self, obj_id: int) -> requests.Response:
        """Удаляет сущность по ее ID с использованием API.

        Args:
        ----------
        obj_id : int
            ID удаляемой сущности.

        Returns:
        ----------
        requests.Response
            Объект ответа запроса.
        """
        return requests.delete(f"{self.URL}{self.DELETE_ENTITY}/{obj_id}")

    def get_entity_by_id(self, obj_id: int) -> requests.Response:
        """Получает сущность по ее ID с использованием API.

        Args:
        ----------
        obj_id : int
            ID искомой сущности.

        Returns:
        ----------
        requests.Response
            Объект ответа запроса.
        """
        return requests.get(f"{self.URL}{self.GET_ENTITY}/{obj_id}")

    def get_all_entities(self) -> requests.Response:
        """Получает все сущности с использованием API.

        Returns:
        ----------
        requests.Response
            Объект ответа запроса.
        """
        return requests.get(f"{self.URL}{self.GET_ALL_ENTITIES}")

    def update_entity_by_id(self, obj_id: int, payload: dict) -> requests.Response:
        """Обновляет сущность по ее ID с использованием API.

        Args:
        ----------
        obj_id : int
            ID обновляемой сущности.
        payload : dict
            Словарь с данными для обновления сущности.

        Returns:
        ----------
        requests.Response
            Объект ответа запроса.
        """
        return requests.patch(f"{self.URL}{self.PATCH_UPDATE_ENTITY}/{obj_id}", json=payload)
