from app import webserver
import pytest


@pytest.fixture
def client():
    app = webserver()
    return app.test_client()


@pytest.fixture
def database(scope='file'):
    db.create_all()


def test_default_route(client):
    response = client.get('/')
    assert response.status == '200 OK'
    assert response.data == b'Hello, World!'


def test_get_services_api_endpoint(client):
    response = client.get('/api/services', data=dict(title='some service title', body='the concrete explanation of the service'))
    assert response.status_code == 200
    assert response.is_json
    assert b'some service title' in response.data


def test_get_a_service_api_endpoint(client):
    response = client.get('/api/services/1')
    assert response.status_code == 200
    assert response.is_json
    assert b'body' in response.data


'''
def test_post_service_api_endpoint(client):
    response = client.get('/api/services/1')
    assert response.status == '200 OK'
'''


def test_get_users_api_endpoint(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert response.is_json
    assert b'username' in response.data


def test_get_a_user_api_endpoint(client):
    response = client.get('/api/users')
    assert response.status_code == 200
    assert response.is_json
    assert b'username' in response.data
