from flask_restful import Api

from api.food import FoodsApi,BmrAPI,FoodApi
from api.authentication import TokenApi,RefreshToken

def create_route(api: Api):

    api.add_resource(TokenApi,'/authentication/token')
    api.add_resource(RefreshToken,'/authentication/token/refresh')

    api.add_resource(FoodsApi, '/foods')
    api.add_resource(FoodApi, '/foods/<name>')

    api.add_resource(BmrAPI,'/bmr')
