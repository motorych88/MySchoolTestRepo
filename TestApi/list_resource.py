import httpx
from jsonschema import validate

from Core.Contracts import RESOURCE_DATA_SCHEMA

URL = 'https://reqres.in/'
LIST_RESOURCE = 'api/unknown'
SINGLE_RESOURCE = 'api/unknown/2'
RESOURCE_NOT_FOUND = 'api/unknown/23'


def test_list_resource():
    response = httpx.get(URL + LIST_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']

    for item in data:
        validate(item, RESOURCE_DATA_SCHEMA)
        assert item['color'].startswith('#')


def test_single_resource():
    response = httpx.get(URL + SINGLE_RESOURCE)
    assert response.status_code == 200
    data = response.json()['data']
    assert data['color'].startswith('#')

def test_resource_not_found():
    response = httpx.get(URL + RESOURCE_NOT_FOUND)
    assert response.status_code == 404