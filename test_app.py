from app import webserver
import pytest


@pytest.fixture
def client():
    app = webserver()
    return app.test_client()


def test_default_route(client):
    response = client.get('/')
    assert response.status == '200 OK'
    assert response.data == b'Hello, World!'


def test_services_api_endpoint(client):
    response = client.get('/api/services')
    assert response.status == '200 OK'


def test_services_slash_id_api_endpoint(client):
    response = client.get('/api/services/1')
    assert response.status == '200 OK'
