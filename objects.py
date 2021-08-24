#Copyright 2020, Alexander Wassell, All rights reserved.

class Category:
    def __init__(self, id=0, name=None):
        self.id = id
        self.name = name

class Product:
    def __init__(self, id=0, code=None, name=None, price=0.0, category=None):
        self.id = id
        self.code = code
        self.name = name
        self.price = price
        self.category = category
