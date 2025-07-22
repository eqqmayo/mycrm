from flask import Blueprint, render_template, request
from database import database_sqlite as db
from utils.pagination import paginate

store_bp = Blueprint('store', __name__)

@store_bp.route('/')
@store_bp.route('/<int:page>')
def store(page=1):
    result = paginate(
        page=page,
        get_count_func=db.get_stores_count,
        get_items_func=db.get_stores_per_page,
    )
    return render_template('pages/store/store.html',
                         stores=result['items'],
                         **result['pagination'],
                         )

@store_bp.route('/detail/<string:id>')
def store_detail(id):
    month = request.args.get('month', '')
    store = db.get_store_by_id(id)

    if month:
        rev = db.get_daily_rev_by_storeid(id, month)
        regular = db.get_monthly_regulars_by_id(id, month)
        return render_template('pages/store/store_detail.html', 
                                store=store, 
                                day_rev=rev,
                                month_regular=regular,
                                month=month,
                                )
    rev = db.get_monthly_rev_by_storeid(id)
    regular = db.get_regulars_by_id(id)
    return render_template('pages/store/store_detail.html', 
                                store=store, 
                                month_rev=rev,
                                regular=regular,
                                month=month,
                                )