import json

import httpx
import pytest
from jsonschema import validate
import allure

from Core.Contracts import REGISTER_SUCCEFUL_SCHEMA, REGISTER_UNSUCCEFUL_SCHEMA, LOGIN_SUCCEFUL_SCHEMA

URL = 'https://reqres.in/'
REGISTER = 'api/register'
LOGIN = 'api/login'

json_file = open('Core/new_users_data.json')
users_data = json.load(json_file)


@allure.suite('Регистрация / Авторизация')
@allure.title('Успешная регистрация')
@pytest.mark.parametrize('users_data', users_data)
def test_register_succeful(users_data):
    with allure.step(f'Делаем запрос по адресу {URL + REGISTER}'):
        response = httpx.post(URL + REGISTER, json=users_data)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 200
    validate(response.json(), REGISTER_SUCCEFUL_SCHEMA)



@allure.suite('Регистрация / Авторизация')
@allure.title('Регистрация без поля пароль')
def test_register_unsucceful_no_password():
    body = {
        "email": "byron.fields@reqres.in"
    }
    with allure.step(f'Делаем запрос по адресу {URL + REGISTER}'):
        response = httpx.post(URL + REGISTER, json=body)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 400
    validate(response.json(), REGISTER_UNSUCCEFUL_SCHEMA)



@allure.suite('Регистрация / Авторизация')
@allure.title('Регистрация без поля почты')
def test_register_unsucceful_no_email():
    body = {
        "password": "pistol"
    }
    with allure.step(f'Делаем запрос по адресу {URL + REGISTER}'):
        response = httpx.post(URL + REGISTER, json=body)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 400
    validate(response.json(), REGISTER_UNSUCCEFUL_SCHEMA)



@allure.suite('Регистрация / Авторизация')
@allure.title('Успешная авторизация')
@pytest.mark.parametrize('users_data', users_data)
def test_login_succeful(users_data):
    with allure.step(f'Делаем запрос по адресу {URL + LOGIN}'):
        response = httpx.post(URL + LOGIN, json=users_data)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 200
    validate(response.json(), LOGIN_SUCCEFUL_SCHEMA)
