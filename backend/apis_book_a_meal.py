from flask import Flask, jsonify, request, make_response
from models import DbUsers, DbCaterers

app = Flask(__name__)
user_db = DbUsers()
caterer_db = DbCaterers()


@app.route('/auth/signup',  methods=['POST'])
def register_user():
    data = request.get_json()
    if data['category'] == 'user':
        if data['password'] == data['confirm_password']:
            if user_db.add_user(data['email'], data['username'], data['password'], data['address']):
                message = '{} successfully signed up.'.format(data['username'])
                message.encode('utf-8')
                return make_response(jsonify(dict(message=message)), 201)



if __name__ == '__main__':
    app.run(debug=True)
