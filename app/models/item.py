from models.user import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column('Id', db.String, primary_key=True)
    name = db.Column('Name', db.String)
    type = db.Column('Type', db.String)
    unitprice = db.Column('UnitPrice', db.String)

    def __init__(self, id, name, type, unitprice):
        self.id = id
        self.name = name 
        self.type = type 
        self.unitprice = unitprice