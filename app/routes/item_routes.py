from flask import Blueprint, render_template, request
import database_sqlite as db

item_bp = Blueprint('item', __name__)

@item_bp.route('/')
def item():
    page = request.args.get('page', default=1, type=int)
    limit = 12
    last_page = db.get_items_count()
    items = db.get_items_per_page(page, limit)
    return render_template('pages/item.html', 
                            items=items,
                            last_page=last_page,
                            current_page=page,
                            )

@item_bp.route('/detail')
def item_detail():
    
    return render_template('pages/user.html')