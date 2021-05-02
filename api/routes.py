from flask_restful import Api

from api.food import FoodsApi


def create_route(api: Api):
    print("create_route")
    api.add_resource(FoodsApi, '/foods') 
