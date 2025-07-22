from flask import Blueprint, render_template
from database import database_sqlite as db
from utils.pagination import paginate

order_bp = Blueprint('order', __name__)

@order_bp.route('/')
@order_bp.route('/<int:page>')
def order(page=1):
    result = paginate(
        page=page,
        get_count_func=db.get_orders_count,
        get_items_func=db.get_orders_per_page,
    )
    return render_template('pages/order/order.html',
                         orders=result['items'],
                         **result['pagination'],
                         )

@order_bp.route('/detail/<string:id>')
def order_detail(id):
    order = db.get_order_by_id(id)
    return render_template('pages/order/order_detail.html', order=order)