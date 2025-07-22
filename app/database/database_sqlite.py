import sqlite3 as sql
from typing import Tuple, Dict, Any
from utils.constants import DATABASE

def get_db():
    db = sql.connect(DATABASE)
    db.row_factory = sql.Row
    return db

def execute_query(query: str, params: Tuple = (), fetch_one: bool = False) -> Dict[str, Any]:
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query, params)
    
    keys = [description[0] for description in cursor.description]
    items = cursor.fetchone() if fetch_one else cursor.fetchall()
    
    db.close()
    return {
        'keys': keys,
        'items': [dict(items)] if items and fetch_one 
            else [dict(item) for item in items] if items 
            else []
    }

def execute_count_query(query: str, params: Tuple = ()) -> int:
    db = get_db()
    cursor = db.cursor()
    cursor.execute(query, params)
    count = cursor.fetchone()[0]
    db.close()
    return count

# Order ============================================================================

def get_orders_per_page(page, limit):
    return execute_query(
        'SELECT * FROM orders LIMIT ? OFFSET ?',
        (limit, (page-1) * limit)
    )

def get_orders_count():
    return execute_count_query('SELECT COUNT(*) FROM orders')

def get_order_by_id(id):
    return execute_query(
        'SELECT * FROM orders WHERE id = ?',
        (id,),
        fetch_one=True
    )

# OrderItem ============================================================================

def get_orderitems_per_page(page, limit):
    return execute_query(
        '''SELECT o.*, i.name 
           FROM orderitems o 
           JOIN items i ON o.itemid = i.id 
           LIMIT ? OFFSET ?''',
        (limit, (page-1) * limit)
    )

def get_orderitems_count():
    return execute_count_query('SELECT COUNT(*) FROM orderitems')

def get_orderitem_by_orderid(id):
    return execute_query(
        '''SELECT o.*, i.name 
           FROM orderitems o 
           JOIN items i ON o.itemid = i.id 
           WHERE o.orderid = ?''',
        (id,)
    )

# Item ============================================================================

def get_items_per_page(page, limit):
    return execute_query(
        'SELECT * FROM items LIMIT ? OFFSET ?',
        (limit, (page-1) * limit)
    )

def get_items_count():
    return execute_count_query('SELECT COUNT(*) FROM items')

def get_item_by_id(id):
    return execute_query(
        'SELECT name, unitprice FROM items WHERE id = ?',
        (id,),
        fetch_one=True
    )

def get_month_rev_by_itemid(id):
    return execute_query(
        '''SELECT strftime('%Y-%m', o.orderat) AS Month, 
                  SUM(i.unitprice) AS "Total Revenue", 
                  COUNT(*) AS "Item Count"
           FROM stores s
           JOIN orders o ON s.id = o.storeid 
           JOIN orderitems oi ON o.id = oi.orderid
           JOIN items i ON oi.itemid = i.id
           WHERE i.id = ?
           GROUP BY Month''',
        (id,)
    )

# Store ============================================================================

def get_stores_per_page(page, limit):
    return execute_query(
        'SELECT * FROM stores LIMIT ? OFFSET ?',
        (limit, (page-1) * limit)
    )

def get_stores_count():
    return execute_count_query('SELECT COUNT(*) FROM stores')

def get_store_by_id(id):
    return execute_query(
        'SELECT name, type, address FROM stores WHERE id = ?',
        (id,),
        fetch_one=True
    )

def get_monthly_rev_by_storeid(id):
    return execute_query(
        '''SELECT strftime('%Y-%m', o.orderat) AS Month, 
                  SUM(i.unitprice) AS Revenue, 
                  COUNT(*) AS Count
           FROM stores s
           JOIN orders o ON s.id = o.storeid 
           JOIN orderitems oi ON o.id = oi.orderid
           JOIN items i ON oi.itemid = i.id
           WHERE s.id = ?
           GROUP BY Month''',
        (id,)
    )

def get_daily_rev_by_storeid(id, month):
    return execute_query(
        '''SELECT strftime('%Y-%m-%d', o.orderat) AS Month, 
                  SUM(i.unitprice) AS Revenue, 
                  COUNT(*) AS Count
           FROM stores s
           JOIN orders o ON s.id = o.storeid 
           JOIN orderitems oi ON o.id = oi.orderid
           JOIN items i ON oi.itemid = i.id
           WHERE s.id = ? AND strftime('%Y-%m', o.orderat) = ?
           GROUP BY Month''',
        (id, month)
    )

def get_regulars_by_id(id):
    return execute_query(
        '''SELECT u.id, u.name, COUNT(*) AS Frequency
           FROM users u 
           JOIN orders o ON u.id = o.userid
           WHERE o.storeid = ?
           GROUP BY u.id
           ORDER BY frequency DESC
           LIMIT 10''',
        (id,)
    )

def get_monthly_regulars_by_id(id, month):
    return execute_query(
        '''SELECT u.id, u.name, COUNT(*) AS Frequency
           FROM users u 
           JOIN orders o ON u.id = o.userid
           WHERE o.storeid = ? AND strftime('%Y-%m', o.orderat) = ?
           GROUP BY u.id
           ORDER BY frequency DESC
           LIMIT 10''',
        (id, month)
    )   