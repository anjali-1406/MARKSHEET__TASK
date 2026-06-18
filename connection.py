import psycopg2

def get_connection():

    conn = psycopg2.connect(
        host="localhost",
        database="studentdb",
        user="postgres",
        password="12345"
    )

    return conn