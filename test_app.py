from app import webserver
import pytest


@pytest.fixture
def client():
    app = webserver()
    return app.test_client()


def test_services_endpoint(client):
    response = client.get('/')
    assert response.status == '200 OK'
    assert response.data == b'Hello, World!'
