import httpx
from jsonschema import validate

from Core.Contracts import USER_DATA_SCHEMA

URL = 'https://reqres.in/'
LIST_USERS = 'api/users?page=2'
EMAIL_ENDS = '@reqres.in'
AVATAR_ENDS = '-image.jpg'
SINGLE_USER = 'api/users/2'
NOT_FOUND = 'api/users/23'


def test_list_users():
    response = httpx.get(URL + LIST_USERS)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, USER_DATA_SCHEMA)
        assert item['email'].endswith(EMAIL_ENDS)
        assert item['avatar'].endswith(str(item['id']) + AVATAR_ENDS)


def test_single_user():
    response = httpx.get(URL + SINGLE_USER)
    assert response.status_code == 200
    data = response.json()['data']
    assert data['email'].endswith(EMAIL_ENDS)
    assert data['avatar'].endswith(str(data['id']) + AVATAR_ENDS)


def test_not_found():
    response = httpx.get(URL + NOT_FOUND)
    assert response.status_code == 404
