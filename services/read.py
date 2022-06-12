from fastapi import FastAPI

from pydantic import BaseModel

from utils.database import Database


app = FastAPI()


@app.get("/{npm}")
async def root(npm: str):
    db = Database()

    sql_select_query = """
        SELECT npm, name FROM students WHERE npm = ?
    """

    try:
        cursor = db.conn.cursor()
        cursor.execute(sql_select_query, (npm,))
        result = cursor.fetchone()

        if result is None:
            return {"status": "NOT_FOUND"}

        return {
            "status": "OK",
            "npm": result[0],
            "name": result[1],
        }

    except:
        return {"status": "ERROR"}
