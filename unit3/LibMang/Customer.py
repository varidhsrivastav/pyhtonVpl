class Customer:
    def __init__(self, name,  address):
        self.name =name
        self.address=address
    def __Str__(self):
        return f" name: {self.name}, Adress: {self.address}"