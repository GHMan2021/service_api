from genetators.entity import EntityGenerator
from lib.module.service_test_api import ServiceTestApi
from lib.service_test_api import check_validate_response
from schemas.entity import Entity
import allure


@allure.feature('ServiceTest')
@allure.title('Получение создание сущности')
@allure.description("""
    Цель: Проверить создание сущности

    Шаги:
    1. Сделать запрос на создание сущности
    2. Проверить статус ответа
    3. Проверить тип возвращаемого ответа""")
def test_create_entity(delete_object):
    with allure.step("Запрос на создание сущности"):
        payload = EntityGenerator.random()
        new_object_endpoint = ServiceTestApi()
        res = new_object_endpoint.create_entity(payload)
        res_txt = res.text
        delete_object.append(res_txt)

    with allure.step("Проверка статуса ответа сервиса"):
        assert res.status_code == 200, f"{res.status_code} - неверный статус код"

    with allure.step("Проверка типа возвращаемого ответа"):
        assert isinstance(res_txt, str), "Не текстовое значение ответа сервиса"
        assert isinstance(int(res_txt), int), "Не числовой id в ответе сервиса"


@allure.feature('ServiceTest')
@allure.title('Удаление сущности')
@allure.description("""
    Цель: Проверить удаление сущности

    Шаги:
    1. Сделать запрос на удаление сущности
    2. Проверить статус ответа""")
def test_delete_entity(create_object):
    with allure.step("Запрос на удаление сущности"):
        obj_id = create_object.text
        delete_obj_endpoint = ServiceTestApi()
        res = delete_obj_endpoint.delete_entity_by_id(obj_id)

    with allure.step("Проверка статуса ответа сервиса"):
        assert res.status_code == 204, f"{res.status_code} - неверный статус код"


@allure.feature('ServiceTest')
@allure.title('Получение сущности')
@allure.description("""
    Цель: Проверить получение сущности

    Шаги:
    1. Сделать запрос на получение сущности
    2. Проверить статус ответа
    3. Валидировать полученные данные""")
def test_get_entity(create_object, delete_object):
    with allure.step("Запрос на получение сущности"):
        obj_id = create_object.text
        delete_object.append(obj_id)

        get_obj_endpoint = ServiceTestApi()
        res = get_obj_endpoint.get_entity_by_id(obj_id)
        res_json = res.json()

    with allure.step("Проверка статуса ответа сервиса"):
        assert res.status_code == 200, f"{res.status_code} - неверный статус код"

    with allure.step("Проверка валидности полученных данных"):
        check_validate_response(res_json, Entity)


@allure.feature('ServiceTest')
@allure.title('Получение всех сущностей')
@allure.description("""
    Цель: Проверить получение всех сущностей

    Шаги:
    1. Сделать запрос на получение всех сущностей
    2. Проверить статус ответа
    3. Валидировать полученные данные""")
def test_get_all_entities(create_object, delete_object):
    with allure.step("Запрос на получение всех сущностей"):
        obj_id = create_object.text
        delete_object.append(obj_id)

        get_all_objs_endpoint = ServiceTestApi()
        res = get_all_objs_endpoint.get_all_entities()
        res_json = res.json().get('entity')

    with allure.step("Проверка статуса ответа сервиса"):
        assert res.status_code == 200, f"{res.status_code} - неверный статус код"

    with allure.step("Проверка валидности полученных данных"):
        check_validate_response(res_json, Entity)


@allure.feature('ServiceTest')
@allure.title('Обновление сущности')
@allure.description("""
    Цель: Проверить обновление сущности

    Шаги:
    1. Сделать запрос на обновление сущности
    2. Проверить статус ответа""")
def test_update_entity(create_object, delete_object):
    with allure.step("Запрос на обновление сущности"):
        obj_id = create_object.text
        delete_object.append(obj_id)

        payload = EntityGenerator.random()
        update_obj_endpoint = ServiceTestApi()
        res = update_obj_endpoint.update_entity_by_id(obj_id, payload)

    with allure.step("Проверка статуса ответа сервиса"):
        assert res.status_code == 204, f"{res.status_code} - неверный статус код"
