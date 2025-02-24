import json

import httpx
import pytest
from jsonschema import validate
import allure

from Core.Contracts import REGISTER_SUCCESSFUL_SCHEMA, ERROR_SCHEMA, LOGIN_SUCCESSFUL_SCHEMA

URL = 'https://reqres.in/'
REGISTER = 'api/register'
LOGIN = 'api/login'

json_file = open('Core/new_users_data.json')
users_data = json.load(json_file)


@allure.suite('Регистрация / Авторизация')
@allure.title('Успешная регистрация')
@pytest.mark.parametrize('users_data', users_data)
def test_register_successfull(users_data):
    with allure.step(f'Делаем запрос по адресу {URL + REGISTER}'):
        response = httpx.post(URL + REGISTER, json=users_data)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 200
    validate(response.json(), REGISTER_SUCCESSFUL_SCHEMA)


@allure.suite('Регистрация / Авторизация')
@allure.title('Регистрация без поля пароль')
def test_register_unsuccessfull_no_password():
    body = {
        "email": "byron.fields@reqres.in"
    }
    with allure.step(f'Делаем запрос по адресу {URL + REGISTER}'):
        response = httpx.post(URL + REGISTER, json=body)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 400
    validate(response.json(), ERROR_SCHEMA)


@allure.suite('Регистрация / Авторизация')
@allure.title('Регистрация без поля почты')
def test_register_unsuccessfull_no_email():
    body = {
        "password": "pistol"
    }
    with allure.step(f'Делаем запрос по адресу {URL + REGISTER}'):
        response = httpx.post(URL + REGISTER, json=body)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 400
    validate(response.json(), ERROR_SCHEMA)


@allure.suite('Регистрация / Авторизация')
@allure.title('Успешная авторизация')
@pytest.mark.parametrize('users_data', users_data)
def test_login_successfull(users_data):
    with allure.step(f'Делаем запрос по адресу {URL + LOGIN}'):
        response = httpx.post(URL + LOGIN, json=users_data)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 200
    validate(response.json(), LOGIN_SUCCESSFUL_SCHEMA)


@allure.suite('Регистрация / Авторизация')
@allure.title('Авторизация без поля пароль')
def test_login_unsuccessfull_no_password():
    body = {
        "email": "peter@klaven"
    }
    with allure.step(f'Делаем запрос по адресу {URL + LOGIN}'):
        response = httpx.post(URL + LOGIN, json=body)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 400
    validate(response.json(), ERROR_SCHEMA)


@allure.suite('Регистрация / Авторизация')
@allure.title('Авторизация без поля почты')
def test_login_unsuccessfull_no_email():
    body = {
        "password": "pistol"
    }
    with allure.step(f'Делаем запрос по адресу {URL + LOGIN}'):
        response = httpx.post(URL + LOGIN, json=body)
    with allure.step('Проверяем статус код'):
        assert response.status_code == 400
    validate(response.json(), ERROR_SCHEMA)
