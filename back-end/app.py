from flask import Flask, jsonify

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

# Temporary in-memory data for categories (mock data).
CATEGORIES = [
    {
        "id": 1,
        "slug": "smartphones",
        "title": "Смартфоны",
        "description": "Смартфоны и аксессуары.",
        "image": "/static/categories/smartphones.jpg",
    },
    {
        "id": 2,
        "slug": "laptops",
        "title": "Ноутбуки",
        "description": "Ноутбуки и ультрабуки.",
        "image": "/static/categories/laptops.jpg",
    },
    {
        "id": 3,
        "slug": "computers",
        "title": "Компьютеры",
        "description": "ПК, системные блоки и моноблоки.",
        "image": "/static/categories/computers.jpg",
    },
    {
        "id": 4,
        "slug": "tvs",
        "title": "Телевизоры",
        "description": "Телевизоры и панели.",
        "image": "/static/categories/tvs.jpg",
    },
    {
        "id": 5,
        "slug": "tablets",
        "title": "Планшеты",
        "description": "Планшеты и аксессуары.",
        "image": "/static/categories/tablets.jpg",
    },
    {
        "id": 6,
        "slug": "speakers",
        "title": "Колонки",
        "description": "Портативные и домашние колонки.",
        "image": "/static/categories/speakers.jpg",
    },
]


@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"


@app.route("/categories")
def categories_list():
    return jsonify({"items": CATEGORIES, "total": len(CATEGORIES)})


if __name__ == "__main__":
    app.run(debug=True)
