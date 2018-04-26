from flask import Flask, jsonify, request, make_response


app = Flask(__name__, instance_relative_config=True)


from api_v1.users import user_page

app.register_blueprint(user_page)

from api_v1.meals import meals
app.register_blueprint(meals)

# ==================== supportive functions===============================


if __name__ == '__main__':
    app.run(debug=True)
