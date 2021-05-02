from flask import Flask
from flask_core import CORS
from falsk_jwt_exceptions.jwt_manager import JWTManager
from flask_resful import Api

from flask_pymongo import pymongo
from flask_mongoengine import MongoEngine


#init app
app = Flask(__name__)

config = {
    'JSON_SORT_KEYS': False,
    'JWT_SECRET_KEY': '&F)J@NcRfUjXn2r5u7x!A%D*G-KaPdSg',
    'JWT_ACCESS_TOKEN_EXPIRES': 300,
    'JWT_REFRESH_TOKEN_EXPIRES': 604800
}

CORS(app, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"
], supports_credentials=True)


app.config.update(config)


#init MongoEngine
db = MongoEngine(app=app)


# init JWT
jwt = JWTManager(app=app)


if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True,use_reloader=True)