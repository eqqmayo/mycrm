from database.database_orm import db

class OrderItem(db.Model):
    __tablename__ = 'orderitems'

    id = db.Column('Id', db.String, primary_key=True)
    orderid = db.Column('OrderId', db.String, db.ForeignKey('orders.Id'))
    itemid = db.Column('ItemId', db.String, db.ForeignKey('items.Id'))
    
    item = db.relationship('Item', backref='orderitems', lazy=True)

    def __init__(self, id, orderid, itemid):
        self.id = id
        self.orderid = orderid 
        self.itemid = itemid