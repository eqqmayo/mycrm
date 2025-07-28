from flask import Blueprint, jsonify, request
from utils.constants import ITEM_LIMIT, PAGE_LIMIT
from models.user import User
from collections import Counter
from math import ceil

user_api_bp = Blueprint('user_api', __name__)

@user_api_bp.route('/')
@user_api_bp.route('/<int:page>')
def get_users(page=1):
    item_limit = ITEM_LIMIT
    page_limit = PAGE_LIMIT
    
    offset = (page - 1) * item_limit

    name = request.args.get('name')
    gender = request.args.get('gender')

    query = User.query

    if name:
        query = query.filter(User.name.like(f'%{name}%')) 
    if gender: 
        query = query.filter(User.gender == gender)

    users = query.offset(offset).limit(item_limit).all()
    total_count = query.count() 
    last_page = ceil(total_count / item_limit)

    start = (ceil(page / page_limit) - 1) * page_limit + 1
    end = min(ceil(page / page_limit) * page_limit, last_page)

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
    user = User.query.filter(User.id == id).one()
    return jsonify([{
        'Name': user.name,
        'Gender': user.gender,
        'Age': user.age,
        'Birthdate': user.birthdate,
        'Address': user.address
    }])

@user_api_bp.route('/orders/<string:id>')
def get_orders_by_id(id):
    user = User.query.filter(User.id == id).one()
    return jsonify([{
        'OrderId': order.id,
        'OrderAt': order.orderat,
        'StoreId': order.storeid,
    } for order in user.orders])

@user_api_bp.route('/goto-stores/<string:id>')
def get_goto_stores_by_id(id):
    user = User.query.filter(User.id == id).one()
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
    user = User.query.filter(User.id == id).one()
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