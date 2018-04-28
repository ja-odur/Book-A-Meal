from flask import jsonify, request, make_response, Blueprint

from models_v1.models import DbOrders

orders_db = DbOrders

orders = Blueprint('orders', __name__, url_prefix='/api/v1')