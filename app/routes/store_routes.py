from flask import Blueprint, render_template, request
import database.database_sqlite as db
from math import ceil

store_bp = Blueprint('store', __name__)

@store_bp.route('/')
@store_bp.route('/<int:page>')
def store(page=1):
    limit = 12
    last_page = ceil(db.get_stores_count() / limit)

    start = (ceil(page / 10) - 1) * 10 + 1
    end = min(ceil(page / 10) * 10, last_page)

    stores = db.get_stores_per_page(page, limit)

    return render_template('pages/store/store.html', 
                            stores=stores,
                            last_page=last_page,
                            current_page=page,
                            start=start,
                            end=end
                            )

@store_bp.route('/detail/<string:id>')
def store_detail(id):
    month = request.args.get('month', '')
    store = db.get_store_by_id(id)

    if month:
        rev = db.get_day_rev_by_storeid(id, month)
        regular = db.get_month_regular_by_id(id, month)
        return render_template('pages/store/store_detail.html', 
                                store=store, 
                                day_rev=rev,
                                month_regular=regular,
                                month=month,
                                )
    rev = db.get_month_rev_by_storeid(id)
    regular = db.get_regular_by_id(id)
    return render_template('pages/store/store_detail.html', 
                                store=store, 
                                month_rev=rev,
                                regular=regular,
                                month=month,
                                )