from flask import Blueprint

from models_v1.models import DbMenu

menu_db = DbMenu()

menu = Blueprint('menu', __name__, url_prefix='/api/v1')
