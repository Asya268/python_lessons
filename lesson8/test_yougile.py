import requests

base_url = "https://ru.yougile.com/"


def get_auth_token():
    creds = {
        'login': '',
        'password': '',
        'companyId': ''
    }
    resp = requests.post(base_url + 'api-v2/auth/keys', json=creds)
    assert resp.status_code == 201
    response_data = resp.json()
    assert "key" in response_data
    token = response_data["key"]
    assert token
    return token


def test_create_project():
    auth_token = get_auth_token()
    project = {
        "title": "Новый Проект",
        "users": {
            "1cf9bc39-51a3-45a4-9e38-b900b07c6791": "admin"
        }
    }
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
    resp = requests.post(
        base_url + 'api-v2/projects',
        json=project,
        headers=headers
    )
    assert resp.status_code == 201
    response_data = resp.json()
    assert 'id' in response_data


def test_create_project_empty_title():
    auth_token = get_auth_token()
    project = {
        "title": "",
        "users": {
            "1cf9bc39-51a3-45a4-9e38-b900b07c6791": "admin"
        }
    }
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
    resp = requests.post(
        base_url + 'api-v2/projects',
        json=project,
        headers=headers
    )
    assert resp.status_code == 400


def test_change_project():
    auth_token = get_auth_token()
    create_data = {
        "title": "Временный Проект",
        "users": {
            "1cf9bc39-51a3-45a4-9e38-b900b07c6791": "admin"
        }
    }
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
    create_resp = requests.post(
        base_url + 'api-v2/projects',
        json=create_data,
        headers=headers
    )
    assert create_resp.status_code == 201
    project_id = create_resp.json()['id']
    update_data = {
        "title": "Обновленный Проект",
        "users": {
            "1cf9bc39-51a3-45a4-9e38-b900b07c6791": "worker"
        },
        "deleted": False
    }
    update_url = f"{base_url}api-v2/projects/{project_id}"
    update_resp = requests.put(
        update_url,
        json=update_data,
        headers=headers
    )
    assert update_resp.status_code == 200


def test_negative_change_project():
    auth_token = get_auth_token()
    create_data = {
        "title": "Временный Проект",
        "users": {
            "1cf9bc39-51a3-45a4-9e38-b900b07c6791": "admin"
        }
    }
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
    create_resp = requests.post(
        base_url + 'api-v2/projects',
        json=create_data,
        headers=headers
    )
    assert create_resp.status_code == 201
    project_id = create_resp.json()['id']
    update_invalid_title = {
        "title": 12345,
        "users": {"1cf9bc39-51a3-45a4-9e38-b900b07c6791": "worker"}
    }
    update_resp = requests.put(
        f"{base_url}api-v2/projects/{project_id}",
        json=update_invalid_title,
        headers=headers
    )
    assert update_resp.status_code == 400


def test_get_project_basic():
    auth_token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }

    # Создаем проект
    create_resp = requests.post(
        base_url + 'api-v2/projects',
        json={"title": "Тест", "users":
              {"1cf9bc39-51a3-45a4-9e38-b900b07c6791": "admin"}},
        headers=headers
    )

    assert create_resp.status_code == 201
    project_id = create_resp.json()['id']

    # GET запрос
    get_resp = requests.get(
        f"{base_url}api-v2/projects/{project_id}", headers=headers)

    # Минимальные проверки
    assert get_resp.status_code == 200
    assert get_resp.json().get('id') == project_id


def test_negative_get_project():
    auth_token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json'
    }
    # Проверяем несуществующий ID
    invalid_id = 'неверный-id'
    get_invalid = requests.get(
        f"{base_url}api-v2/projects/{invalid_id}",
        headers=headers
    )
    assert get_invalid.status_code == 404
