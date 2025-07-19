from flask import Blueprint, render_template, request
import database_sqlite as db
from math import ceil

order_bp = Blueprint('order', __name__)

@order_bp.route('/')
@order_bp.route('/<int:page>')
def order(page=1):
    limit = 12
    last_page = ceil(db.get_orders_count() / limit)

    start = (ceil(page / 10) - 1) * 10 + 1
    end = min(ceil(page / 10) * 10, last_page)

    orders = db.get_orders_per_page(page, limit)
    return render_template('pages/order/order.html', 
                            orders=orders,
                            last_page=last_page,
                            current_page=page,
                            start=start,
                            end=end
                            )

@order_bp.route('/detail/<string:id>')
def order_detail(id):
    order = db.get_order_by_id(id)
    return render_template('pages/order/order_detail.html', order=order)