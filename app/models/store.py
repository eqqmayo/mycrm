from models.user import db

class Store(db.Model):
    __tablename__ = 'stores'

    id = db.Column('Id', db.String, primary_key=True)
    name = db.Column('Name', db.String)
    type = db.Column('Type', db.String)
    address = db.Column('Address', db.String)

    def __init__(self, id, name, type, address):
        self.id = id
        self.name = name 
        self.type = type 
        self.address = address