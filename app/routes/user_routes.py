from flask import Blueprint, render_template, jsonify, request
from models.user import User
from collections import Counter
from math import ceil


user_bp = Blueprint('user', __name__)
user_api_bp = Blueprint('user_api', __name__)

# ------------------------------------------------------
@user_bp.route('/')
def user():
    return render_template('pages/user/user.html')

@user_bp.route('/detail/<string:id>')
def user_detail(id):
    return render_template('pages/user/user_detail.html')

# -------------------------------------------------------
@user_api_bp.route('/')
@user_api_bp.route('/<int:page>')
def get_users(page=1):
    limit = 12
    offset = (page - 1) * limit

    query = User.query

    name = request.args.get('name')
    gender = request.args.get('gender')

    if name:
        query = query.filter(User.name.like(f'%{name}%')) 
    if gender: 
        query = query.filter(User.gender == gender)

    users = query.offset(offset).limit(limit).all()
    total_count = query.count()  # 필터링된 전체 수
    last_page = ceil(total_count / limit)

    start = (ceil(page / 10) - 1) * 10 + 1
    end = min(ceil(page / 10) * 10, last_page)

    return jsonify({
        'users':[{
            'Id': user.id,
            'Name': user.name,
            'Gender': user.gender,
            'Age': user.age,
            'Birthdate': user.birthdate,
        } for user in users],
        'pagination':{
            'current_page': page,
            'last_page': last_page,
            'start': start,
            'end': end,
        }
    })

@user_api_bp.route('/user/<string:id>')
def get_user_by_id(id):
    user = User.query.filter_by(id=id).one()
    return jsonify([{
        'Name': user.name,
        'Gender': user.gender,
        'Age': user.age,
        'Birthdate': user.birthdate,
        'Address': user.address
    }])

@user_api_bp.route('/orders/<string:id>')
def get_orders_by_id(id):
    user = User.query.filter_by(id=id).one()
    return jsonify([{
        'OrderId': order.id,
        'OrderAt': order.orderat,
        'StoreId': order.storeid,
    } for order in user.orders])

@user_api_bp.route('/goto-stores/<string:id>')
def get_goto_stores_by_id(id):
    user = User.query.filter_by(id=id).one()
    store_count = Counter()

    for order in user.orders:
        if order.store: 
            store_count[order.store.name] += 1

    top_stores = store_count.most_common(5)
    
    return jsonify([{
        'Store': store,
        'Count': count,
    } for store, count in top_stores])

@user_api_bp.route('/goto-items/<string:id>')
def get_goto_items_by_id(id):
    user = User.query.filter_by(id=id).one()
    item_count = Counter()

    for order in user.orders:
        for orderitem in order.orderitems:  
            if orderitem.item:  
                item_count[orderitem.item.name] += 1
            
    top_items = item_count.most_common(5)
    
    return jsonify([{
        'Item': item,
        'Count': count,
    } for item, count in top_items])