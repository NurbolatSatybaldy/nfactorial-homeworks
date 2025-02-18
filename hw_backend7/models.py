class User:
    def __init__(self, id, email, full_name, password_hash, photo_url=None):
        self.id = id
        self.email = email
        self.full_name = full_name
        self.password_hash = password_hash
        self.photo_url = photo_url

class Flower:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

class Purchase:
    def __init__(self, id, user_id, flower_id):
        self.id = id
        self.user_id = user_id
        self.flower_id = flower_id
