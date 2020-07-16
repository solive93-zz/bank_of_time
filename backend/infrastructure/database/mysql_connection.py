import pymysql


class MySQLConnection:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1dos3quatre",
            db="banc_del_temps"
        )

        self.cursor = self.connection.cursor()

