from flask import Blueprint, render_template
import database.database_sqlite as db
from math import ceil

orderitem_bp = Blueprint('orderitem', __name__)

@orderitem_bp.route('/')
@orderitem_bp.route('/<int:page>')
def orderitem(page=1):
    limit = 12
    last_page = ceil(db.get_orderitems_count() / limit)

    start = (ceil(page / 10) - 1) * 10 + 1
    end = min(ceil(page / 10) * 10, last_page)

    orderitems = db.get_orderitems_per_page(page, limit)
    return render_template('pages/orderitem/orderitem.html', 
                            orderitems=orderitems,
                            last_page=last_page,
                            current_page=page,
                            start=start,
                            end=end
                            )

@orderitem_bp.route('/detail/<string:id>')
def orderitem_detail(id):
    orderitem = db.get_orderitem_by_orderid(id)
    return render_template('pages/orderitem/orderitem_detail.html', orderitem=orderitem)
