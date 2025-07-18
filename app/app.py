from flask import Flask, redirect, url_for
from models.user import db
from models.order import Order
from models.item import Item
from models.store import Store
from models.orderitem import OrderItem
import os

from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.user_routes import user_api_bp
from routes.order_routes import order_bp
from routes.orderitem_routes import orderitem_bp
from routes.item_routes import item_bp
from routes.store_routes import store_bp

app = Flask(__name__)

db_path = os.path.join(os.path.dirname(__file__), 'mycrm.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(user_api_bp, url_prefix='/api/users')
app.register_blueprint(order_bp, url_prefix='/orders')
app.register_blueprint(orderitem_bp, url_prefix='/orderitems')
app.register_blueprint(item_bp, url_prefix='/items')
app.register_blueprint(store_bp, url_prefix='/stores')

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
