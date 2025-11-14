from flask import Blueprint, jsonify
from .db import get_connection

products_bp = Blueprint("products", __name__)

@products_bp.route("/products", methods=["GET"])
def get_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data), 200


@products_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
    data = cursor.fetchone()

    cursor.close()
    conn.close()

    if not data:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(data), 200
