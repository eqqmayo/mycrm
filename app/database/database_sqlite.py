import sqlite3 as sql

DATABASE = 'mycrm.db'

# order --------------------------------------------------------------------------------------
def get_db():
    db = sql.connect(DATABASE)
    db.row_factory = sql.Row
    return db

def get_orders_per_page(page, limit):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM orders LIMIT ? OFFSET ?', (limit, (page-1) * limit))
    keys = [description[0] for description in cursor.description]
    items = cursor.fetchall()
    db.close()
    return {'keys': keys, 'items': [dict(item) for item in items]}

def get_orders_count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT COUNT(*) FROM orders')
    count = cursor.fetchone()[0]
    db.close()
    return count

def get_order_by_id(id: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM orders WHERE id = ?', (id,))
    keys = [description[0] for description in cursor.description]
    item = cursor.fetchone()
    db.close()
    return {'keys': keys, 'items': [dict(item)]}

# order item --------------------------------------------------------------------------------------

def get_orderitems_per_page(page, limit):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'SELECT o.*, i.name FROM orderitems o JOIN items i ON o.itemid = i.id LIMIT ? OFFSET ?', 
        (limit, (page-1) * limit)
    )
    keys = [description[0] for description in cursor.description]
    items = cursor.fetchall()
    db.close()
    return {'keys': keys, 'items': [dict(item) for item in items]}

def get_orderitems_count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT COUNT(*) FROM orderitems')
    count = cursor.fetchone()[0]
    db.close()
    return count

def get_orderitem_by_orderid(id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'SELECT o.*, i.name FROM orderitems o JOIN items i ON o.itemid = i.id WHERE o.orderid = ?', (id,) 
    )
    keys = [description[0] for description in cursor.description]
    items = cursor.fetchall()
    db.close()
    return {'keys': keys, 'items': [dict(item) for item in items]}

# item --------------------------------------------------------------------------------------

def get_items_per_page(page, limit):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM items LIMIT ? OFFSET ?', (limit, (page-1) * limit))
    keys = [description[0] for description in cursor.description]
    items = cursor.fetchall()
    db.close()
    return {'keys': keys, 'items': [dict(item) for item in items]}

def get_items_count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT COUNT(*) FROM items')
    count = cursor.fetchone()[0]
    db.close()
    return count

def get_item_by_id(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT name, unitprice FROM items WHERE id = ?', (id,))
    keys = [description[0] for description in cursor.description]
    item = cursor.fetchone()
    db.close()
    return {'keys': keys, 'items': [dict(item)]}

def get_month_rev_by_itemid(id: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT strftime('%Y-%m', o.orderat) AS Month, 
               SUM(i.unitprice) AS "Total Revenue", 
               COUNT(*) AS "Item Count"
        FROM stores s
        JOIN orders o ON s.id = o.storeid 
        JOIN orderitems oi ON o.id = oi.orderid
        JOIN items i ON oi.itemid = i.id
        WHERE i.id = ?
        GROUP BY Month
        ''', 
        (id,)
    )
    keys = [description[0] for description in cursor.description]
    items = cursor.fetchall()
    db.close()
    return {'keys': keys, 'items': [dict(item) for item in items]}


# store --------------------------------------------------------------------------------------

def get_stores_per_page(page, limit):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM stores LIMIT ? OFFSET ?', (limit, (page-1) * limit))
    keys = [description[0] for description in cursor.description]
    items = cursor.fetchall()
    db.close()
    return {'keys': keys, 'items': [dict(item) for item in items]}

def get_stores_count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT COUNT(*) FROM stores')
    count = cursor.fetchone()[0]
    db.close()
    return count

def get_store_by_id(id: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT name, type, address FROM stores WHERE id = ?', (id,))
    keys = [description[0] for description in cursor.description]
    item = cursor.fetchone()
    db.close()
    return {'keys': keys, 'items': [dict(item)]}

def get_month_rev_by_storeid(id: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT strftime('%Y-%m', o.orderat) AS Month, 
               SUM(i.unitprice) AS Revenue, 
               COUNT(*) AS Count
        FROM stores s
        JOIN orders o ON s.id = o.storeid 
        JOIN orderitems oi ON o.id = oi.orderid
        JOIN items i ON oi.itemid = i.id
        WHERE s.id = ?
        GROUP BY Month
        ''', 
        (id,)
    )
    keys = [description[0] for description in cursor.description]
    items = cursor.fetchall()
    db.close()
    return {'keys': keys, 'items': [dict(item) for item in items]}

def get_day_rev_by_storeid(id: str, month: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT strftime('%Y-%m-%d', o.orderat) AS Month, 
               SUM(i.unitprice) AS Revenue, 
               COUNT(*) AS Count
        FROM stores s
        JOIN orders o ON s.id = o.storeid 
        JOIN orderitems oi ON o.id = oi.orderid
        JOIN items i ON oi.itemid = i.id
        WHERE s.id = ? AND strftime('%Y-%m', o.orderat) = ?
        GROUP BY Month
        ''', 
        (id, month)
    )
    keys = [description[0] for description in cursor.description]
    items = cursor.fetchall()
    db.close()
    return {'keys': keys, 'items': [dict(item) for item in items]}

def get_regular_by_id(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT u.id, u.name, COUNT(*) AS Frequency
        FROM users u 
        JOIN orders o ON u.id = o.userid
        WHERE o.storeid = ?
        GROUP BY u.id
        ORDER BY frequency DESC
        LIMIT 10
        ''', 
        (id,)
    )
    keys = [description[0] for description in cursor.description]
    items = cursor.fetchall()
    db.close()
    return {'keys': keys, 'items': [dict(item) for item in items]}

def get_month_regular_by_id(id, month):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT u.id, u.name, COUNT(*) AS Frequency
        FROM users u 
        JOIN orders o ON u.id = o.userid
        WHERE o.storeid = ? AND strftime('%Y-%m', o.orderat) = ?
        GROUP BY u.id
        ORDER BY frequency DESC
        LIMIT 10
        ''', 
        (id, month)
    )
    keys = [description[0] for description in cursor.description]
    items = cursor.fetchall()
    db.close()
    return {'keys': keys, 'items': [dict(item) for item in items]}