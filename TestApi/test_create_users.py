import httpx
from jsonschema import validate
import allure
from Core.Contracts import CREATED_USER_SCHEMA, UPDATE_USER_SCHEMA
import datetime
from Core.api_endpoints import URL

URL = 'https://reqres.in/'
CREATE = 'api/users'
UPDATE = 'api/users/2'


@allure.suite('Работа с Юзерами')
@allure.title('Проверка создание юзера')
def test_create_user():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    with allure.step(f'Делаем запрос по адресу {URL + CREATE}'):
        response = httpx.post(URL + CREATE, json=body)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 201
    creation_date = response.json()['createdAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    validate(response.json(), CREATED_USER_SCHEMA)
    with allure.step('Проверяем, что тело в ответе правильное'):
        assert response.json()['name'] == body['name']
        assert response.json()['job'] == body['job']
    with allure.step('Проверяем, что дата в ответе правильная'):
        assert creation_date[0:16] == current_date[0:16]


@allure.suite('Работа с Юзерами')
@allure.title('Проверка редактирования юзера методом PUT')
def test_update_put_user():
    body = {
        "name": "morpheus",
        "job": "zion resident"
    }
    with allure.step(f'Делаем запрос по адресу {URL + UPDATE}'):
        response = httpx.put(URL + UPDATE, json=body)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 200
    updated_date = response.json()['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    validate(response.json(), UPDATE_USER_SCHEMA)
    with allure.step('Проверяем, что тело в ответе правильное'):
        assert response.json()['name'] == body['name']
        assert response.json()['job'] == body['job']
    with allure.step('Проверяем, что дата в ответе правильная'):
        assert updated_date[0:16] == current_date[0:16]


@allure.suite('Работа с Юзерами')
@allure.title('Проверка редактирования юзера методом PATCH')
def test_update_patch_user():
    body = {
        "name": "morpheus"
    }
    with allure.step(f'Делаем запрос по адресу {URL + UPDATE}'):
        response = httpx.patch(URL + UPDATE, json=body)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 200
    updated_date = response.json()['updatedAt'].replace('T', ' ')
    current_date = str(datetime.datetime.utcnow())
    validate(response.json(), UPDATE_USER_SCHEMA)
    with allure.step('Проверяем, что тело в ответе правильное'):
        assert response.json()['name'] == body['name']
    with allure.step('Проверяем, что дата в ответе правильная'):
        assert updated_date[0:16] == current_date[0:16]


@allure.suite('Работа с Юзерами')
@allure.title('Проверка удаления юзера')
def test_delete_user():
    with allure.step(f'Делаем запрос по адресу {URL + UPDATE}'):
        response = httpx.delete(URL + UPDATE)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 204
