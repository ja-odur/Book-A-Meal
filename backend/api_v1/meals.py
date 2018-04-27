from flask import jsonify, request, make_response, Blueprint
from ..models import DbMeals

meals_db = DbMeals()

meals = Blueprint('meals', __name__, url_prefix='/api/v1')