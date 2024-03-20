from typing import List, Union, Dict

from faker import Faker

fake = Faker('ru-RU')


class AdditionGenerator:
    """Класс для генерации дополнительной информации.

    Methods:
    ----------
    random() -> Dict[str, Union[int, str]]:
        Генерирует случайный словарь с дополнительной информацией.

    Attributes:
    ----------
    fake : Faker
        Экземпляр Faker для генерации фальшивых данных.
    """
    @staticmethod
    def random() -> Dict[str, Union[int, str]]:
        """Генерирует случайный словарь с дополнительной информацией.

        Returns:
        ----------
        Dict[str, Union[int, str]]:
            Словарь, содержащий случайную дополнительную информацию с ключами:
                - 'additional_info': Строка с произвольной текстовой информацией.
                - 'additional_number': Целое случайное число от 0 до 100.
        """
        additional_info = fake.text()
        additional_number = fake.random_int(0, 100)
        return {
            "additional_info": additional_info,
            "additional_number": additional_number
        }


class EntityGenerator:
    """Класс для генерации сущностей.

    Methods:
    ----------
    random() -> Dict[str, Union[str, List[int], bool, AdditionGenerator]]:
        Генерирует случайный словарь с информацией о сущности.

    Attributes:
    ----------
    fake : Faker
        Экземпляр Faker для генерации фальшивых данных.
    """
    @staticmethod
    def random() -> Dict[str, Union[str, List[int], bool, AdditionGenerator]]:
        """Генерирует случайный словарь с информацией о сущности.

        Returns:
        ----------
        Dict[str, Union[str, List[int], bool, AdditionGenerator]]:
            Словарь, содержащий случайную информацию о сущности с ключами:
                - 'important_numbers': Список целых чисел от 0 до 100 в количестве от 1 до 5
                - 'title': Строка со случайным словом
                - 'verified': Булево значение
                - 'addition': Объект AdditionGenerator, представляющий дополнительную информацию о сущности.
        """
        important_numbers = [fake.random_int(0, 100) for _ in range(fake.random_int(1, 5))]
        title = fake.word()
        verified = fake.boolean()
        addition = AdditionGenerator.random()
        return {
            "important_numbers": important_numbers,
            "title": title,
            "verified": verified,
            "addition": addition
        }
