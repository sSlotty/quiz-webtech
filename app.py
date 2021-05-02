from flask import Flask
from flask_cors import CORS
from flask_jwt_extended.jwt_manager import JWTManager
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy

from api.routes import create_route
 
config = {
    'JSON_SORT_KEYS': False,
    'JWT_SECRET_KEY': '&F)J@NcRfUjXn2r5u7x!A%D*G-KaPdSg',
    'JWT_ACCESS_TOKEN_EXPIRES': 300,
    'JWT_REFRESH_TOKEN_EXPIRES': 604800
}

#init app
app = Flask(__name__)


CORS(app, origins="*", allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"
], supports_credentials=True)


app.config.update(config)

api = Api(app)
create_route(api=api)


# init JWT
jwt = JWTManager(app=app)


if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True,use_reloader=True)