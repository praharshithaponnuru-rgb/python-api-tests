import os
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ["REQRES_API_KEY"]

@pytest.fixture
def api_headers():
    return {"x-api-key": API_KEY}

def test_get_users_with_valid_key(api_headers):
    resp = requests.get("https://reqres.in/api/users?page=2", headers=api_headers)
    assert resp.status_code == 200
    body = resp.json()
    assert "data" in body
    assert len(body["data"]) > 0

def test_collections_without_key_fails():
    resp = requests.get("https://reqres.in/api/collections/products/records")
    assert resp.status_code in (400, 401)
