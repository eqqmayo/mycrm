from flask import Flask, redirect, url_for

from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.order_routes import order_bp
from routes.orderitem_routes import orderitem_bp
from routes.item_routes import item_bp
from routes.store_routes import store_bp

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(order_bp, url_prefix='/orders')
app.register_blueprint(orderitem_bp, url_prefix='/orderitems')
app.register_blueprint(item_bp, url_prefix='/items')
app.register_blueprint(store_bp, url_prefix='/stores')

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
