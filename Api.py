from flask import Flask, send_file
from flask_cors import CORS

import config

from db import db

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return "Girlcode Store API"

@app.route('/categories')
def categories_route():
    tmp_categories = []

    cat_instance = db('categories')

    rows = cat_instance.select()

    for row in rows:
        tmp_cat = {
            "id": row[0],
            "name": row[1],
            "slug": row[2],
            "desc": row[3],
            "img": row[4]
        }

        tmp_categories.append(tmp_cat)

    categories_dict = {
        "categories": tmp_categories
    }

    return categories_dict

@app.route('/category/<cat_slug>')
def category_route(cat_slug):
    cat_instance = db('categories')

    rows = cat_instance.select(f"WHERE slug='{cat_slug}'")

    if len(rows):
        row = rows[0]

        tmp_cat = {
            "id": row[0],
            "name": row[1],
            "slug": row[2],
            "desc": row[3],
            "img": row[4]
        }

        return tmp_cat
    else:
        return {}
    

@app.route('/products')
def products_route():
    prod_instance = db('products')

    tmp_products = []

    rows = prod_instance.select()

    for row in rows:
        tmp_prod = {
            "id": row[0],
            "prod_name": row[1],
            "prod_img": row[2],
            "prod_desc": row[3],
            "prod_slug": row[4],
            "prod_price": row[5]
        }

        tmp_products.append(tmp_prod)

    products_dict = {
        "products": tmp_products
    }

    return products_dict


@app.route('/product/<prod_slug>')
def product_route(prod_slug):
    prod_instance = db('products')

    rows = prod_instance.select(f"WHERE prod_slug='{prod_slug}'")

    if len(rows):
        row = rows[0]

        tmp_prod = {
            "id": row[0],
            "prod_name": row[1],
            "prod_img": row[2],
            "prod_desc": row[3],
            "prod_slug": row[4],
            "prod_price": row[5]
        }

        return tmp_prod
    else:
        return {}

@app.route('/image/<img_name>')
def get_image(img_name):
    filename = f'images/{img_name}'

    return send_file(filename, mimetype='image/jpg')
