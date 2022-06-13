from utils.database import Database


db = Database()

sql_create_table = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name VARCHAR(256) NOT NULL,
        npm VARCHAR(32) NOT NULL UNIQUE
    );
"""

db.conn.cursor().execute(sql_create_table)
