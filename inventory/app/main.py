from flask import Flask, jsonify
from shop_common.validation import normalize

app = Flask(__name__)
STOCK = {"laptop": 5, "mouse": 100, "keyboard": 40}

@app.route("/")
def home():
    return "Inventory service running"

@app.route("/stock/<item>")
def stock(item):
    name = normalize(item)
    if name not in STOCK:
        return jsonify(error="Unknown item"), 404
    return jsonify(item=name, stock=STOCK[name])