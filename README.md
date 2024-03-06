## Установка и запуск проекта
Проект тестирования точек доступа для управления сущностями в базе данных PostgreSQL. Включает конфигурацию Docker Compose для настройки сервиса, базы данных и миграций. Сервис API доступен на github по 
[ссылке](https://github.com/sun6r0/test-service "Сервис API")  


1. Склонировать репозиторий
```
git clone https://github.com/GHMan2021/service_api.git
```
2. Перейти в директорию проекта
3. Создать виртуальное окружение
```
python -m venv venv
```
4. Активировать окружение
```
venv\Scripts\activate
```
5. Установка зависимостей
```
pip install -r requirements.txt
```
6. Запуск тестов
```
pytest --alluredir=allure-results
```
7. Запуск отчета allure по тестам
```
allure serve allure-results
```