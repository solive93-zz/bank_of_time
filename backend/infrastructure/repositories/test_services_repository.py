from backend.infrastructure.repositories.services_repository import ServicesRepository
import pytest

def test_fetch_by_id_query_is_build_with_the_id_passed():
    repo = ServicesRepository()
    sql_query = "SELECT * FROM services WHERE id='1'"
    assert repo.fetch_by_id(1) == sql_query
