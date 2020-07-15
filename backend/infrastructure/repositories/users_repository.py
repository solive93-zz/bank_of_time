from backend.domain.user import User
from backend.infrastructure.database.mysql_connection import MySQLConnection
from backend.infrastructure.repositories.sql_repository_interface import SQLRepositoryInterface


class UsersRepository(SQLRepositoryInterface, MySQLConnection):

    def get_by_id(self, user_id: int):
        return "SELECT * FROM users WHERE id={}".format(user_id)

    def get_all(self):
        return "SELECT * FROM users"

    def create(self, user: User):
        sql_query = "INSERT INTO users VALUES({}, '{}', '{}', '{}')".format(
            user.id,
            user.username,
            user.email,
            user.password
        )
        return sql_query

    def update(self, user: User, username: str, password: str):
        return "UPDATE users SET username='{}', password='{}' WHERE id={}".format(username, password, user.id)

    def delete(self, user_id: int):
        return "DELETE FROM users WHERE id={}".format(user_id)

    def execute_query(self, sql_query: str):
        try:
            self.cursor.execute(sql_query)

            if 'WHERE' in sql_query:
                user = self.cursor.fetchone()
                return User(user[0], user[1], user[2], user[3])

            users = self.cursor.fetchall()
            all_users = []
            for user in users:
                new_user = User(user[0], user[1], user[2], user[3])
                all_users.append(new_user)
            return all_users

        except Exception as e:
            raise e

    def save_changes(self, sql_query: str):
        try:
            self.cursor.execute(sql_query)
            self.connection.commit()
        except Exception as e:
            raise e
