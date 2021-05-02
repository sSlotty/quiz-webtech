from flask import Flask
import sqlalchemy
from flask_core import CORS
from falsk_jwt_exceptions.jwt_manager import JWTManager
from flask_resful import Api

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#init app
app = Flask(__name__)

config = {
    'JSON_SORT_KEYS': False,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///food_db.db',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'JWT_SECRET_KEY': '&F)J@NcRfUjXn2r5u7x!A%D*G-KaPdSg',
    'JWT_ACCESS_TOKEN_EXPIRES': 300,
    'JWT_REFRESH_TOKEN_EXPIRES': 604800
}

CORS(app, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"
], supports_credentials=True)


app.config.update(config)


db.init_app(app)

# init JWT
jwt = JWTManager(app=app)


if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True,use_reloader=True)