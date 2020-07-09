import mysql.connector

database = mysql.connector.connect(host="localhost", user="root", password="1dos3quatre", database="banc_del_temps")

cursor = database.cursor()
