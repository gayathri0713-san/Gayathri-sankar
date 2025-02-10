from Flask import Flask, request, jsonify

app = Flask(__name__)

# Sample menu
menu = {
    1: {"name": "Pasta", "price": 250},
    2: {"name": "Pizza", "price": 300},
    3: {"name": "Burger", "price": 150},
    4: {"name": "Coffee", "price": 100}
}

# Store orders
orders = []

@app.route('/menu', methods=['GET'])
def get_menu():
    """Retrieve the hotel menu"""
    return jsonify(menu)

@app.route('/order', methods=['POST'])
def place_order():
    """Place an order"""
    data = request.json  # Get JSON data from request
    item_id = data.get("item_id")
    quantity = data.get("quantity")

    if item_id not in menu:
        return jsonify({"error": "Item not found"}), 404

    item = menu[item_id]
    total_price = item["price"] * quantity

    order = {
        "item": item["name"],
        "quantity": quantity,
        "total_price": total_price
    }
    orders.append(order)

    return jsonify({"message": "Order placed successfully", "order": order})

@app.route('/orders', methods=['GET'])
def get_orders():
    """Retrieve all orders"""
    return jsonify(orders)

if __name__ == '__main__':
    app.run(debug=True)
