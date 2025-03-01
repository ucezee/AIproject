import sqlite3
import os


def get_db_connection():
    conn = sqlite3.connect( os.getenv("DBNAME") )
    conn.row_factory = sqlite3.Row
    return conn
