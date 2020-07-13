from mysql.connector import cursor

from backend.domain.service import Service
from backend.infrastructure.repositories.sql_repository_interface import SQLRepositoryInterface
from backend.infrastructure.database.mysql_connection import MySQLConnection


class ServicesRepository(SQLRepositoryInterface):

    cursor = MySQLConnection.mysql_connect()

    def fetch_all(self):
        cursor.execute("SELECT * FROM services")

    def fetch_one(self, service: Service):
        query = "SELECT + FROM services WHERE id=%s"
        cursor.execute(query, id)

    def create(self, service: Service):
        pass

    def update(self, service: Service):
        pass

    def destroy(self, service: Service):
        pass
