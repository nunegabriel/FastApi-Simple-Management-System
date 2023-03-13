import psycopg2
from fastapi import FastAPI

app = FastAPI()

# db details
db_name = "testing"
db_user = "postgres"
db_password ='lgreqwr720'
db_host = "localhost"
db_port = "5432"


def get_db():
    """
    Open a new database connection and return a cursor object.
    """
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )
    cursor = conn.cursor()
    return cursor

@app.post("/add-data")
def add_data(name: str, event: str):
    """
    Add a new record to the database.
    """
    cursor = get_db()
    cursor.execute("INSERT INTO events (name, event) VALUES (%s, %s);", (name, event))
    cursor.connection.commit()
    cursor.close()
    return {"status": "ok", "message": "Data added successfully."}