from fastapi import FastAPI

from pydantic import BaseModel

from utils.database import Database


class Student(BaseModel):
    name: str
    npm: str


app = FastAPI()


@app.post("/")
async def root(student: Student):
    db = Database()

    sql_insert_query = """
        INSERT INTO students (name, npm)
        VALUES (?, ?)
    """

    try:
        cursor = db.conn.cursor()
        cursor.execute(sql_insert_query, (student.name, student.npm))
        db.conn.commit()

        return {"status": "OK"}

    except:
        db.conn.rollback()
        return {"status": "ERROR"}
