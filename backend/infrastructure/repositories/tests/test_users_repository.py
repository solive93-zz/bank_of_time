from backend.domain.user import User
from backend.infrastructure.repositories.users_repository import UsersRepository


def test_get_by_id_query_is_build_with_the_id_given():
    repo = UsersRepository()
    sql_query = "SELECT * FROM users WHERE id=5"
    assert repo.get_by_id(5) == sql_query


def test_get_all_query_is_build():
    repo = UsersRepository()
    sql_query = "SELECT * FROM users"
    assert repo.get_all() == sql_query


def test_create_user_query_is_built_with_user_data_provided():
    user = User(1, 'solive93', 'solive93@mail.com', '12345')
    repo = UsersRepository()
    sql_query = "INSERT INTO users VALUES(1, 'solive93', 'solive93@mail.com', '12345')"
    assert repo.create(user) == sql_query


def test_update_user_query_is_built_with_args_given():
    user = User(2, 'solif', 'solif@mail.com', 'pilota')
    repo = UsersRepository()
    sql_query = "UPDATE users SET username='solive', password='qwerty' WHERE id=2"
    assert repo.update(user, 'solive', 'qwerty') == sql_query


def test_delete_query_is_build_with_the_id_given():
    repo = UsersRepository()
    sql_query = "DELETE FROM users WHERE id=300"
    assert repo.delete(300) == sql_query
