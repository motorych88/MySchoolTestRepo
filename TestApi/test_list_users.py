import httpx
from jsonschema import validate
from Core.Contracts import USER_DATA_SCHEMA
import allure


URL = 'https://reqres.in/'
LIST_USERS = 'api/users?page=2'
EMAIL_ENDS = '@reqres.in'
AVATAR_ENDS = '-image.jpg'
SINGLE_USER = 'api/users/2'
NOT_FOUND = 'api/users/23'


@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение списка пользователей')
def test_list_users():
    with allure.step(f'Делаем запрос по адресу {URL + LIST_USERS}'):
        response = httpx.get(URL + LIST_USERS)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        with allure.step(f'Проверяем элемент из списка'):
            validate(item, USER_DATA_SCHEMA)
            with allure.step('Проверяем окончание email'):
                assert item['email'].endswith(EMAIL_ENDS)
            with allure.step('Проверяем, что id есть в поле "avatar"'):
                assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)


@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение пользователя')
def test_single_user():
    with allure.step(f'Делаем запрос по адресу {URL + SINGLE_USER}'):
        response = httpx.get(URL + SINGLE_USER)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 200
    data = response.json()['data']
    validate(data, USER_DATA_SCHEMA)
    with allure.step('Проверяем окончание email'):
        assert data['email'].endswith(EMAIL_ENDS)
    with allure.step('Проверяем, что id есть в поле "avatar"'):
        assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)


@allure.suite('Проверка запросов данных пользователей')
@allure.title('Проверяем получение, если пользователя не существует')
def test_not_found():
    with allure.step(f'Делаем запрос по адресу {URL + NOT_FOUND}'):
        response = httpx.get(URL + NOT_FOUND)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 404
