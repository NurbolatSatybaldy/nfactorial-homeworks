from passlib.hash import bcrypt

class User:
    def __init__(self, id, email, full_name, password_hash, photo_url=None):
        self.id = id
        self.email = email
        self.full_name = full_name
        self.password_hash = password_hash
        self.photo_url = photo_url

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)

class Flower:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
