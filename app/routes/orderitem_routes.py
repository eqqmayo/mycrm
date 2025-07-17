from flask import Blueprint, render_template, request
import database_sqlite as db

orderitem_bp = Blueprint('orderitem', __name__)

@orderitem_bp.route('/')
def orderitem():
    page = request.args.get('page', default=1, type=int)
    limit = 12
    last_page = db.get_orderitems_count()
    orderitems = db.get_orderitems_per_page(page, limit)
    return render_template('pages/orderitem.html', 
                            orderitems=orderitems,
                            last_page=last_page,
                            current_page=page,
                            )

@orderitem_bp.route('/detail')
def orderitem_detail():
    
    return render_template('pages/user.html')
