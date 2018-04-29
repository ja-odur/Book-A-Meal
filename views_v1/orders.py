from flask import jsonify, request, make_response, Blueprint

from models_v1.models import DbOrders

orders_db = DbOrders()

orders = Blueprint('orders', __name__, url_prefix='/api/v1')

@orders.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    if data['caterer'] and data['meal']:
        new_order = orders_db.add_order('default', data['caterer'], data['meal'])

        if new_order:
            message = 'Order {} successfully placed.'.format(data)
            return make_response(jsonify(message=message), 201)
    return make_response(jsonify(message='Invalid request format'), 403)
