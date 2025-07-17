from flask import Blueprint, render_template, request
import database_sqlite as db

order_bp = Blueprint('order', __name__)

@order_bp.route('/')
def order():
    page = request.args.get('page', default=1, type=int)
    limit = 12
    last_page = db.get_orders_count()
    orders = db.get_orders_per_page(page, limit)
    return render_template('pages/order.html', 
                            orders=orders,
                            last_page=last_page,
                            current_page=page,
                            )

@order_bp.route('/detail')
def order_detail():
    
    return render_template('pages/user.html')