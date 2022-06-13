from utils.database import Database

db = Database()
cursor = db.conn.cursor()

sql_insert_query = """
    INSERT INTO students (name, npm)
    VALUES (?, ?)
"""

initial_npm_int = 10000000000000000000

counter = 0
num_of_data = 10000000

while counter < num_of_data:
    if (counter % 100000) == 0:
        print("remaining data:", num_of_data - counter)

    npm = str(initial_npm_int + counter)
    name = "Student Name - " + npm

    try:
        cursor.execute(sql_insert_query, (name, npm))

    except Exception as e:
        pass

    counter += 1

db.conn.commit()
