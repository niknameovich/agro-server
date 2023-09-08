import pytest
from os import listdir
from os.path import isfile, join, splitext
from pytest import MonkeyPatch

from fastapi.testclient import TestClient
from fastapi import status, HTTPException

from agro_server.app.main import app

@pytest.fixture
def app_routes():
    return [{"path": route.path, "name": route.name} for route in app.routes]

@pytest.fixture
def get_client():
    return TestClient(app)

@pytest.fixture
def get_dir_routes():
    source_path = 'agro_server/routers'
    onlyfiles = [splitext(f)[0] for f in listdir(source_path) if isfile(join(source_path, f) and not f.startswith('_'))]
    return onlyfiles

@pytest.fixture
def client_response_routes(get_client):
    with get_client as client:
        return client.get('/url-list-from-request').json()

def test_app_include_routers_onstartup(get_client, app_routes):
    with get_client as client:
        response = client.get('/url-list-from-request')
        assert response.status_code == 200
        client_routes = response.json()
    assert len((client_routes)) > len(app_routes)

def test_endpoint_list_after_init(get_dir_routes, client_response_routes):
    endpoint_names = [item['path'].split('/')[1] for item in client_response_routes]
    assert set(get_dir_routes).issubset(endpoint_names)
    
def test_all_endpoints_contains_alive_handle(get_client,client_response_routes):
    with get_client as client:
        for path, name, tags in client_response_routes:
            if 'liveness' in tags: 
                response = get_client.get(path)
                assert response.status_code == 200


def test_auth_is_working(get_client):
    with get_client as client: 
        with pytest.raises(HTTPException):
            response = client.get('\issecure')
            assert response.status_code == 401

def test_correct_auth(get_client):
    # get token from keycloak server
    # paste token to X-Headers 
    # test middleware on /secure endpoint 
    # test middleware on \unsecure endpoint
    pass