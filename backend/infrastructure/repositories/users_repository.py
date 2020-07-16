from backend.domain.user import User
from backend.infrastructure.database.mysql_connection import MySQLConnection
from backend.infrastructure.repositories.sql_repository_interface import SQLRepositoryInterface
import json

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
                result = self.cursor.fetchone()
                user = {'id': result[0],
                        'username': result[1],
                        'email': result[3],
                        'password': result[2],
                        }
                return user

            users = self.cursor.fetchall()
            all_users = []
            for user in users:
                new_user = {'id': user[0],
                            'username': user[1],
                            'email': user[3],
                            'password': user[2],
                            }
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
