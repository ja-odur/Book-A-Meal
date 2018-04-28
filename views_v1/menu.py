from flask import jsonify, request, make_response, Blueprint

from models_v1.models import DbMenu

menu_db = DbMenu()

menu = Blueprint('menu', __name__, url_prefix='/api/v1')


@menu.route('/menu/', methods=['POST'])
def create_menu():
    data = request.get_json()
    created_menu = menu_db.create_menu(caterer='default', daily_menu=data['menu'])

    if created_menu:
        return make_response(jsonify(message=data['menu']), 201)
    return make_response(jsonify(message='Bad data format'), 403)

