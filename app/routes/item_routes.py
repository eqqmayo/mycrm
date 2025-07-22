from flask import Blueprint, render_template
from database import database_sqlite as db
from utils.pagination import paginate
from utils.constants import ITEM_LIMIT

item_bp = Blueprint('item', __name__)

@item_bp.route('/')
@item_bp.route('/<int:page>')
def item(page=1):
    result = paginate(
        page=page,
        get_count_func=db.get_items_count,
        get_items_func=db.get_items_per_page,
    )
    return render_template('pages/item/item.html',
                         items=result['items'],
                         **result['pagination'],
                         )

@item_bp.route('/detail/<string:id>')
def item_detail(id):
    item = db.get_item_by_id(id)
    rev = db.get_month_rev_by_itemid(id)
    return render_template('pages/item/item_detail.html', 
                            item=item,
                            month_rev=rev,
                            )
