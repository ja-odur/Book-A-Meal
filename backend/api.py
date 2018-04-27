from flask import Flask, jsonify, request, make_response
import sys
sys.path.append('backend')




app = Flask(__name__)


from api_v1.users import user_page

app.register_blueprint(user_page)

# ==================== supportive functions===============================


if __name__ == '__main__':
    app.run(debug=True)
