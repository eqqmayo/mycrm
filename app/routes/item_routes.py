from flask import Blueprint, render_template
from ..database import database_sqlite as db
from math import ceil

item_bp = Blueprint('item', __name__)

@item_bp.route('/')
@item_bp.route('/<int:page>')
def item(page=1):
    limit = 12
    last_page = ceil(db.get_items_count() / limit)

    start = (ceil(page / 10) - 1) * 10 + 1
    end = min(ceil(page / 10) * 10, last_page)

    items = db.get_items_per_page(page, limit)
    return render_template('pages/item/item.html', 
                            items=items,
                            last_page=last_page,
                            current_page=page,
                            start=start,
                            end=end
                            )

@item_bp.route('/detail/<string:id>')
def item_detail(id):
    item = db.get_item_by_id(id)
    rev = db.get_month_rev_by_itemid(id)
    return render_template('pages/item/item_detail.html', item=item, month_rev=rev)
