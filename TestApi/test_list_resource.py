import httpx
from jsonschema import validate
from Core.Contracts import RESOURCE_DATA_SCHEMA
import allure

URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
RESOURCE_NOT_FOUND = 'api/unknown/23'


@allure.suite('Проверка запросов ресурса')
@allure.title('Проверяем получение списка ресурсов')
def test_list_resource():
    with allure.step(f'Делаем запрос по адресу {URL + LIST_RESOURCE}'):
        response = httpx.get(URL + LIST_RESOURCE)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step(f'Проверяем элемент из списка'):
            validate(item, RESOURCE_DATA_SCHEMA)
            with allure.step('Проверяем, что поле "color" начинается с #'):
                assert item['color'].startswith('#')


@allure.suite('Проверка запросов ресурса')
@allure.title('Проверяем получения ресурса')
def test_single_resource():
    with allure.step(f'Делаем запрос по адресу {URL + SINGLE_RESOURCE}'):
        response = httpx.get(URL + SINGLE_RESOURCE)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 200
    data = response.json()['data']
    validate(data, RESOURCE_DATA_SCHEMA)
    with allure.step('Проверяем, что поле "color" начинается с #'):
        assert data['color'].startswith('#')


@allure.suite('Проверка запросов ресурса')
@allure.title('Проверяем получение, если ресурса не существует')
def test_resource_not_found():
    with allure.step(f'Делаем запрос по адресу {URL + RESOURCE_NOT_FOUND}'):
        response = httpx.get(URL + RESOURCE_NOT_FOUND)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 404
