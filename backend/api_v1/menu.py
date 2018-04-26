from flask import jsonify, request, make_response, Blueprint
from models import DbMenu

menu_db = DbMenu()

menu = Blueprint('menu', __name__, url_prefix='/api/v1')
