import pytest
from pytest import MonkeyPatch

from fastapi.testclient import TestClient
from fastapi import status, HTTPException

from agro_server.app.main import app
import requests

@pytest.fixture
def get_client():
    return TestClient(app)

@pytest.fixture
def keycloak_realm_config():
    return {'host':'http://localhost:8282','port':8282, 'realm':'agro_'}


hand_generated_keycloak_info = {"realm":"agro_realm",
                                "public_key":
                                "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlwpA9ejSi0hkVc8DCsXfKqUIrZqpsGAKJc7snloGbZA0IzHHsbIqdhGiKbt0eJg2+TrJXIsv659jgN2OjMkueR5LqudKA88YeeDvBmX7PkVWBUdS/fnCiYZK8jCaYs2tyb6sJQ02uXn0DYofx3EPvDIOrpffY8m/rk3K/L3f17z7ffEH2IYf7Q9yS/S6JyGTnuV90K58xIXQWtd/aeVzyHRRZC8r7h8sRF4t4lCuJuqeOyQbBKyDvPEMIQz7+Q8rMvZF6174+S3khTVyE7XwtUOx+h0sLExhOHmG3wCfOczLX+kdP0f+pKX+AA463OyZ7PPdmBstpHT6lW9ax2vdqwIDAQAB"
                                ,"token-service":"http://localhost:8282/realms/agro_realm/protocol/openid-connect","account-service":"http://localhost:8282/realms/agro_realm/account","tokens-not-before":0}

# monkeypatched requests.get moved to a fixture

def test_realm_exists(keycloak_realm_config):
    response = requests.get(f"{keycloak_realm_config['host']}:{keycloak_realm_config['port']}/realms/{keycloak_realm_config['realm']}_realm")
    assert response.status_code == 200
    assert 'public_key' in response.json().keys()
    assert response.json()['public_key'] == hand_generated_keycloak_info['public_key']

def test_user_exists():
    response = requests.post('http://localhost:8282/realms/agro_realm/')
    

#wait an expiration period than try to get something from app 
def test_token_expiration():
    pass

# get access token, change payload, encode again, try to get something from app 
def test_wrong_payload():
    pass 

# get access token, change algorythm to null, change payload, encode, try to get something from app 
def test_null_algorythm():
    pass

# get access token, get ExpirationException, get RefreshToken, try to get something from app 
def test_refresh_token_is_valid():
    pass

# get something from app without scope, try to get something with scope
def test_roles_acceess():
    pass


# get something from app with scope and specific group 
def test_role_and_group():
    pass