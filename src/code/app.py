from flask import Flask,jsonify,request
from flask_restful import Api,Resource
from flask_jwt import JWT,jwt_required

from security import authenticate,identity
#APP    
app = Flask(__name__)
app.secret_key = 'yngwie'

 

# API
api = Api(app)
jwt = JWT(app,authenticate,identity) # /auth


items=[]

class Item(Resource):
    
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda c: c['name']==name,items),None)
        return {'item':item},200 if item else 404
    
    @jwt_required()
    def post(self,name):
        if next(filter(lambda c: c['name']==name,items),None):
            return {'message':"An item with name '{}' already eist".format(name)},400
        data = request.get_json()
        item:{'name':name,'price':data['price']}
        items.append(item)
        return item,201

class Items(Resource):
    @jwt_required()
    def get(self):
        return items



api.add_resource(Item,'/item/<string:name>') # http://127.0.0.1:5000/student/<string:name>
api.add_resource(Items,'/items')
app.run(port=5000)

