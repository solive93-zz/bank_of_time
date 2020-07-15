from backend.domain.service import Service
from backend.infrastructure.repositories.sql_repository_interface import SQLRepositoryInterface
from backend.infrastructure.database.mysql_connection import MySQLConnection


class ServicesRepository(SQLRepositoryInterface, MySQLConnection):

    def get_by_id(self, service_id: int):
        return "SELECT * FROM services WHERE id={}".format(service_id)

    def get_all(self):
        return "SELECT * FROM services"

    def create(self, service: Service):
        sql_query = "INSERT INTO services VALUES({}, '{}', '{}', {})".format(
            service.id,
            service.title,
            service.body,
            service.user_id
        )
        return sql_query

    def update(self, service: Service, title: str, body: str):
        return "UPDATE services SET title='{}', body='{}' WHERE id={}".format(title, body, service.id)

    def delete(self, service_id: int):
        return "DELETE FROM services WHERE id={}".format(service_id)

    def execute_query(self, sql_query: str):
        try:
            self.cursor.execute(sql_query)

            if 'WHERE' in sql_query:
                service = self.cursor.fetchone()
                return Service(service[0], service[1], service[2], service[3])

            services = self.cursor.fetchall()
            all_services=[]
            for service in services:
                new_service = Service(service[0], service[1], service[2], service[3])
                all_services.append(new_service)
            return all_services

        except Exception as e:
            raise e

    def save_changes(self, sql_query: str):
        try:
            self.cursor.execute(sql_query)
            self.connection.commit()
        except Exception as e:
            raise e
