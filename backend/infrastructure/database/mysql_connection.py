import mysql.connector

class MySQLConnection:
    @staticmethod
    def mysql_connect():
        database = mysql.connector.connect(host="localhost", user="root", password="1dos3quatre", database="banc_del_temps")
        cursor = database.cursor()
        return cursor
