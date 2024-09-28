import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена!')

    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    db.commit()

async def insert_products(name_product,category_product, size_product, price_product,
                          product_id,photo):
    with sqlite3.connect('db/store.sqlite3') as db_with:
        cursor_with = db_with.cursor()
    cursor.execute(queries.INSERT_PRODUCTS_QUERY, (
        name_product,
        category_product,
        size_product,
        price_product,
        product_id,
        photo
    ))
    db.commit()
