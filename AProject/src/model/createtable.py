from model.db import get_db_connection
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
schema_path = os.path.join(current_dir, 'schema.sql')

conn = get_db_connection()
cursor = conn.cursor()
with open(schema_path, 'r') as f:
    cursor.executescript(f.read())


conn.commit()
cursor.close()
conn.close()
