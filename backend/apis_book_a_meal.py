from flask import Flask, jsonify, request, make_response
from .models import DbUsers, DbCaterers

app = Flask(__name__)
user_db = DbUsers()
caterer_db = DbCaterers()


@app.route('/auth/signup',  methods=['POST'])
def register_user():
    data = request.get_json()
    if data['password'] == data['confirm_password']:
        if data['category'] == 'user':
            if user_db.add_user(data['email'], data['username'], data['password'], data['address']):
                message = '{} successfully signed up.'.format(data['username'])
                message.encode('utf-8')
                return make_response(jsonify(dict(message=message)), 201)
            else:
                message = '{} already exists.'.format(data['username'])
                message.encode('utf-8')
                return make_response(jsonify(dict(error=message)), 401)

        elif data['category'] == 'caterer':
            if caterer_db.add_user(data['email'], data['username'], data['password'], data['address'],
                                   brand_name='easy_brand'):
                message = '{} successfully signed up.'.format(data['username'])
                return make_response(jsonify(dict(message=message)), 201)


@app.route('/auth/login',  methods=['POST'])
def login():
    data = request.get_json()
    if data['category'] == 'user':
        username = data['username']
        user_info = DbUsers.get_user(username)
        if user_info:
            user_password = user_info['password']
            if user_password == data['password']:
                return make_response(jsonify({'message':'user successfully logged in in'}), 401)

if __name__ == '__main__':
    app.run(debug=True)
