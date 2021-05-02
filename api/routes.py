from flask_resful import Api

from api.foods import FoodsApi


def create_route(api: Api):

    api.add_resource(FoodsApi,'/foods')