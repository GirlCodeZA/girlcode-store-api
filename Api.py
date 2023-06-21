from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return "Girlcode Store API"

@app.route('/categories')
def categories_route():
    tmp_categories = [
        {
            "name": "Furniture",
            "path": "/category/furniture"
        },
        {
            "name": "Hand Bag",
            "path": "/category/hand-bag"
        },
        {
            "name": "Books",
            "path": "/category/books"
        },
        {
            "name": "Tech",
            "path": "/category/tech"
        },
        {
            "name": "Sneakers",
            "path": "/category/sneaker"
        },
        {
            "name": "Travel",
            "path": "/category"
        }
    ]

    categories_dict = {
        "categories": tmp_categories
    }

    return categories_dict

