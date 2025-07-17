from flask import Blueprint, render_template, request
import database_sqlite as db

store_bp = Blueprint('store', __name__)

@store_bp.route('/')
def store():
    page = request.args.get('page', default=1, type=int)
    limit = 12
    last_page = db.get_stores_count()
    stores = db.get_stores_per_page(page, limit)
    return render_template('pages/store.html', 
                            stores=stores,
                            last_page=last_page,
                            current_page=page,
                            )

@store_bp.route('/detail/<string:id>')
def store_detail(id):
    month = request.args.get('month', '')
    store = db.get_store_by_id(id)

    if month:
        rev = db.get_day_rev_by_id(id, month)
        regular = db.get_month_regular_by_id(id, month)
        return render_template('pages/store_detail.html', 
                                store=store, 
                                day_rev=rev,
                                regular=regular,
                                month=month,
                                )
    rev = db.get_month_rev_by_id(id)
    return render_template('pages/store_detail.html', 
                                store=store, 
                                month_rev=rev,
                                month=month,
                                )