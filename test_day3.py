import requests

def test_get_user_success():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200

def test_get_user_not_found():
    response = requests.get("https://reqres.in/api/users/999")
    assert response.status_code == 404

def test_create_user():
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post("https://reqres.in/api/users", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus"