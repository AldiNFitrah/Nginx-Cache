import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.conn = self.create_connection("database.db")
        self.cursor = self.conn.cursor()

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(db_file)
            return conn

        except Error as e:
            print(e)

        return None
