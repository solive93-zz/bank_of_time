from mysql.connector import cursor

from backend.domain.service import Service
from backend.infrastructure.repositories.sql_repository_interface import SQLRepositoryInterface
from backend.infrastructure.database.mysql_connection import MySQLConnection


class ServicesRepository(SQLRepositoryInterface):

    cursor = MySQLConnection.mysql_connect()

    def fetch_all(self):
        cursor.execute("SELECT * FROM banc_del_temps.services")

    def fetch_one(self, id: int):
        query = ("SELECT * FROM banc_del_temps.services WHERE id=%s")
        data = (id)
        service = cursor.execute(query, data)
        return service

    def create(self, service: Service):
        query = "INSERT INTO banc_del_temps.services(id, title, body) VALUES(%s, '%s', '%s')"
        data = (service.id, service.title, service.body)
        cursor.execute(query, data)

    def update(self, service: Service):
        pass

    def destroy(self, service: Service):
        pass
