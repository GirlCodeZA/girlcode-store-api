from psycopg2 import pool

conn_pool = pool.SimpleConnectionPool(
    1, 30,
    database="",
    host="localhost",
    port="5432",
    user="postgres",
    password=""
)

class db:
    def __init__(self, table):
        self.table = table
        self.pool = conn_pool

    def select(self):
        conn = self.pool.getconn()
        cursor = conn.cursor()

        cursor.execute(f'SELECT * FROM {self.table} ORDER BY id ASC')

        rows = cursor.fetchall()

        conn.close()

        return rows