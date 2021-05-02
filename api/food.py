from flask import request,jsonify,Response,current_app
from flask_restful import Resource
from flask_jwt_extended import jwt_required


from models.foods import Foods


class FoodsApi(Resource):

    def get(self)-> Response:
        foods = Foods.query.all();
        response = jsonify(foods)
        response.status_code = 200
        return Response(response)