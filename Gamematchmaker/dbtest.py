import psycopg2
from db_config import DB_CONFIG

conn = psycopg2.connect(**DB_CONFIG)

cur = conn.cursor()
cur.execute("SELECT * FROM games;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
