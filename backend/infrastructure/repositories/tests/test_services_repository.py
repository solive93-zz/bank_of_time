from backend.domain.service import Service
from backend.infrastructure.repositories.services_repository import ServicesRepository


def test_get_by_id_query_is_build_with_the_id_given():
    repo = ServicesRepository()
    sql_query = "SELECT * FROM services WHERE id=1"
    assert repo.get_by_id(1) == sql_query


def test_get_all_query_is_build():
    repo = ServicesRepository()
    sql_query = "SELECT * FROM services"
    assert repo.get_all() == sql_query


def test_create_service_query_is_built_with_service_data_provided():
    service = Service(1, 'hola', 'soy el bola', 1)
    repo = ServicesRepository()
    sql_query = "INSERT INTO services VALUES(1, 'hola', 'soy el bola', 1)"
    assert repo.create(service) == sql_query


def test_update_service_query_is_built_with_2_args_given():
    service = Service(2, 'cocino', 'hago sushi', 1)
    repo = ServicesRepository()
    sql_query = "UPDATE services SET title='canto', body='cantos Gregorianos' WHERE id=2"
    assert repo.update(service, 'canto', 'cantos Gregorianos') == sql_query


def test_delete_query_is_build_with_the_id_given():
    repo = ServicesRepository()
    sql_query = "DELETE FROM services WHERE id=32"
    assert repo.delete(32) == sql_query

