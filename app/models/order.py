from models.user import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column('Id', db.String, primary_key=True)
    orderat = db.Column('OrderAt', db.String)
    storeid = db.Column('StoreId', db.String, db.ForeignKey('stores.Id'))
    userid = db.Column('UserId', db.String, db.ForeignKey('users.Id'))

    store = db.relationship('Store', backref='orders', lazy=True)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

    def __init__(self, id, orderat, storeid, userid):
        self.id = id
        self.orderat = orderat 
        self.storeid = storeid 
        self.userid = userid