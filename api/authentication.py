from flask import request,Response,jsonify,current_app
from flask_restful import Resource

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)

import json
from models.oauth.error import OAuthErrorResponse
from models.oauth.token import TokenResponse


class TokenApi(Resource):
    def post(self)->Response:
        body = request.form.to_dict()
        if body.get('username') is None or body.get('password') is None:
            response = jsonify(
                OAuthErrorResponse(
                    "invalid_request", "The request is missing a required parameter."
                ).__dict__
            )
            response.status_code = 400
            return response
        
        with open('User.json','r') as food:
            data = food.read()

        obj = json.loads(data)
        if obj['username'] == body.get('username') and obj['password'] == body.get('password'):
            return generate_token_response(body.get('username'))
        else:
            response = jsonify(
            OAuthErrorResponse(
                "invalid_request", "Username or password not correct"
            ).__dict__
        )
        response.status_code = 204
        return response

class RefreshToken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        user = get_jwt_identity()
        return generate_token_response(user)


def generate_token_response(user:str)->Response:
    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    response = jsonify(
        TokenResponse(
            access_token=access_token,
            token_type="bearer",
            expires_in=current_app.config['JWT_ACCESS_TOKEN_EXPIRES'],
            refresh_token=refresh_token
        ).__dict__
    )

    response.status_code = 200
    return response