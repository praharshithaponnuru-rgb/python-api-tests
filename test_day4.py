import pytest
import requests

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

def test_get_user(base_url):
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200

def test_get_users_list(base_url):
    response = requests.get(f"{base_url}/users?page=2")
    assert response.status_code == 200