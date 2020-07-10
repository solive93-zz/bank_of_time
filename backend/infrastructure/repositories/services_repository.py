from mysql.connector import cursor

from backend.infrastructure.repositories.sql_repository_interface import SQLRepositoryInterface
from backend.infrastructure.database.mysql_connection import MySQLConnection


class ServicesRepository(SQLRepositoryInterface):

    cursor = MySQLConnection.mysql_connect()

    def fetch_all(self):
        cursor.execute("SELECT * FROM services")

    def fetch_by_id(self, id: int):
        query = "SELECT + FROM services WHERE id=%s"
        cursor.execute(query, id)

    def create(self, id: int):
        pass

    def update(self, id: int):
        pass

    def destroy(self, id: int):
        pass
