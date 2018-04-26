from flask import jsonify, request, make_response, Blueprint
from models import DbMeals

meals_db = DbMeals()

meals = Blueprint('meals', __name__, url_prefix='/api/v1')


@meals.route('/meals/', methods=['POST'])
def create_meal():
    data = request.get_json()

    if meals_db.add_meal(data['username'], data['name'], data['price']):
        message = 'Meal {} successfully added.'.format(data['name'])
        return make_response(jsonify(dict(message=message)), 201)
    else:
        return make_response(jsonify(dict(message='meal not added.')), 401)

@meals.route('/meals/', methods=["GET"])
def get_all_meals():
    meals_per_caterer = meals_db.get_all_meals(caterer='default')

    return make_response(jsonify(message=meals_per_caterer), 201)