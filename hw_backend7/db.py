import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(host="localhost", dbname="flowers", user="nurbolat", password="968510", cursor_factory=RealDictCursor)

def init_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email TEXT UNIQUE NOT NULL, full_name TEXT NOT NULL, password_hash TEXT NOT NULL, photo_url TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS flowers (id SERIAL PRIMARY KEY, name TEXT NOT NULL, quantity INTEGER, price NUMERIC)")
    cur.execute("CREATE TABLE IF NOT EXISTS purchases (id SERIAL PRIMARY KEY, user_id INTEGER NOT NULL, flower_id INTEGER NOT NULL)")
    conn.commit()
    cur.close()
    conn.close()

