from flask import request,jsonify,Response,current_app
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import json


class FoodsApi(Resource):

    def get(self)-> Response:
        if 'name' in request.args:
            name = request.args.get('name')
            data = readJsonFile()
            res = None
            obj = json.loads(data)
            for i in obj:
                if i['Name'] == name:
                    res = i
                    break
            res = jsonify(res)
            res.status_code = 200
            return res
        elif 'calories' in request.args:
            calories = request.args.get('calories')
            data = readJsonFile()
            print(type(calories))
            res = None
            obj = json.loads(data)
            response = list()
            for i in obj:
                if int(calories) >=i['Kilocalories']:
                    x = {
                        'name':i['Name'],
                        'Kilocalories': i['Kilocalories']
                    }
                    response.append(x)

            res = jsonify(response)
            res.status_code = 200
            return res
        else:
            return Response(status=204)

    @jwt_required()
    def post(self)->Response:
        body = request.get_json()
        print(body)
        read = readJsonFile()
        obj = json.loads(read)
        data = list()
        for i in obj:
            data.append(i)
        
        if len(body) > 0:
            data.append(body)

        with open('food_db.json','w') as outfile:
            json.dump(data, outfile)
            response = jsonify(data)
            response.status_code = 200
            return response
    
    @jwt_required()
    def put(self)->Response:
        body = request.get_json()
        key = body['key']
        read = readJsonFile()
        obj = json.loads(read)
        isSucess = False
        data = list()
        for i in obj:
            data.append(i)
            if i['Name'] == key:
                data.remove(i)
                isSucess = True

        del body['key']
        data.append(body)

        if isSucess is True:
            with open('food_db.json','w') as outfile:
                json.dump(data, outfile)
                response = jsonify(data)
                response.status_code = 200
                return response
        else:
            return Response(status=204)
    

class FoodApi(Resource):

    @jwt_required()
    def delete(self,name: str)->Response:
        key = name
        read = readJsonFile()
        obj = json.loads(read)
        data = list()
        isSucess = False
        for i in obj:
            data.append(i)
            if i['Name'] == key:
                data.remove(i)
                isSucess = True

        with open('food_db.json','w') as outfile:
            json.dump(data, outfile)

        if isSucess is True:
            response = jsonify(data)
            response.status_code = 200;
            return response
        else:
            return Response(status=204)

class BmrAPI(Resource):
    def get(self)-> Response:
        gender = request.args.get('gender')
        height = float(request.args.get('height'))
        weight = float(request.args.get('weight'))
        age = int(request.args.get('age'))
    
        if gender.upper() == 'M':
            bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
        elif gender.upper() == 'G':
            bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        else:
            Response(status_code=204)
        
        bmr = round(bmr)
        data = {'bmr':bmr}
        res = jsonify(data)
        res.status_code = 200
        return res

def readJsonFile():
    with open('food_db.json','r') as food:
            data = food.read()
    return data