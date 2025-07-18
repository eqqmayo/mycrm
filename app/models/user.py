from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column('Id', db.String, primary_key=True)
    name = db.Column('Name', db.String)
    gender = db.Column('Gender', db.String)
    age = db.Column('Age', db.String)
    birthdate = db.Column('Birthdate', db.String)
    address = db.Column('Address', db.String)
    
    orders = db.relationship('Order', backref='user', lazy=True)

    def __init__(self, id, name, gender, age, birthdate, address):
        self.id = id
        self.name = name 
        self.gender = gender 
        self.age = age
        self.birthdate = birthdate
        self.address = address

    def __str__(self):
        return f"User('id': {self.id}, 'name': {self.name}, 'gender': {self.gender}, 'age': {self.age}, 'birthdate': {self.birthdate}, 'address': {self.address})"
