import os, json, urllib.request
from flask import Flask, jsonify
from shop_common.pricing import total_with_tax
from shop_common.validation import normalize

app = Flask(__name__)
INVENTORY_URL = os.getenv("INVENTORY_URL", "http://localhost:8001")
PRICES = {"laptop": 900.0, "mouse": 25.0, "keyboard": 60.0}

def get_stock(item):
    with urllib.request.urlopen(f"{INVENTORY_URL}/stock/{item}", timeout=3) as r:
        return json.loads(r.read())["stock"]

@app.route("/")
def home():
    return "Orders service running"

@app.route("/order/<item>/<int:qty>")
def order(item, qty):
    name = normalize(item)
    if name not in PRICES:
        return jsonify(error="Unknown item"), 404
    try:
        stock = get_stock(name)
    except Exception:
        return jsonify(error="Inventory unavailable"), 503
    if qty > stock:
        return jsonify(error="Insufficient stock", available=stock), 409
    return jsonify(item=name, qty=qty, total=total_with_tax(PRICES[name] * qty))