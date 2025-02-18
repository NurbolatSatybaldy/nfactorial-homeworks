from db import get_connection
from models import User, Flower, Purchase

class UsersRepository:
    def create_user(self, email, full_name, password_hash, photo_url):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (email, full_name, password_hash, photo_url) VALUES (%s, %s, %s, %s) RETURNING id", (email, full_name, password_hash, photo_url))
        user_id = cur.fetchone()["id"]
        conn.commit()
        cur.close()
        conn.close()
        return user_id

    def get_user_by_email(self, email):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, email, full_name, password_hash, photo_url FROM users WHERE email = %s", (email,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return User(row["id"], row["email"], row["full_name"], row["password_hash"], row["photo_url"])
        return None

    def get_user_by_id(self, user_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, email, full_name, password_hash, photo_url FROM users WHERE id = %s", (user_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return User(row["id"], row["email"], row["full_name"], row["password_hash"], row["photo_url"])
        return None

class FlowersRepository:
    def create_flower(self, name, quantity, price):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO flowers (name, quantity, price) VALUES (%s, %s, %s) RETURNING id", (name, quantity, price))
        flower_id = cur.fetchone()["id"]
        conn.commit()
        cur.close()
        conn.close()
        return flower_id

    def get_all_flowers(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, quantity, price FROM flowers ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [Flower(row["id"], row["name"], row["quantity"], row["price"]) for row in rows]

    def get_flower_by_id(self, flower_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, quantity, price FROM flowers WHERE id = %s", (flower_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return Flower(row["id"], row["name"], row["quantity"], row["price"])
        return None

class PurchasesRepository:
    def add_purchase(self, user_id, flower_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO purchases (user_id, flower_id) VALUES (%s, %s)", (user_id, flower_id))
        conn.commit()
        cur.close()
        conn.close()

    def get_purchases_by_user(self, user_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT f.id, f.name, f.price FROM purchases p JOIN flowers f ON p.flower_id = f.id WHERE p.user_id = %s", (user_id,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
