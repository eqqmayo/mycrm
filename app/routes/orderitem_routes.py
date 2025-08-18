from flask import Blueprint, Response, render_template
import database.database_sqlite as db
from utils.pagination import paginate

orderitem_bp = Blueprint('orderitem', __name__)

@orderitem_bp.route('/')
@orderitem_bp.route('/<page>')
def orderitem(page=1):
    result = paginate(
        page=page,
        endpoint='orderitem.orderitem',
        get_count_func=db.get_orderitems_count,
        get_items_func=db.get_orderitems_per_page,
    )
    
    if isinstance(result, Response):
        return result

    return render_template('pages/orderitem/orderitem.html',
                            orderitems=result['items'],
                            **result['pagination'],
                            )

@orderitem_bp.route('/detail/<string:id>')
def orderitem_detail(id):
    orderitem = db.get_orderitem_by_orderid(id)
    return render_template('pages/orderitem/orderitem_detail.html', orderitem=orderitem)
