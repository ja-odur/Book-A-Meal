from flask import Flask

app = Flask(__name__, instance_relative_config=True)


from app_v1.views.users import users

app.register_blueprint(users)

from app_v1.views.meals import meals
app.register_blueprint(meals)

from app_v1.views.menu import menu
app.register_blueprint(menu)

from app_v1.views.orders import orders
app.register_blueprint(orders)



if __name__ == '__main__':
    app.run(debug=True)
