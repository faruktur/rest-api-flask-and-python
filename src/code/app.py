from flask import Flask,jsonify,request
from flask_restful import Api,Resource,reqparse
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
    parser= reqparse.RequestParser()
    parser.add_argument('price',type=float,required=true,
    help="This field is required"
    )
    
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda c: c['name']==name,items),None)
        return {'item':item},200 if item else 404
    
    @jwt_required()
    def post(self,name):
        if next(filter(lambda c: c['name']==name,items),None):
            return {'message':"An item with name '{}' already eist".format(name)},400
        data = Item.parser.parse_args()
        item:{'name':name,'price':data['price']}
        items.append(item)
        return item,201
    
    @jwt_required()
    def delete(self,name):
        global items
        item = list(filter(lambda c:c['name']!=name,items))
        items.remove(item)
        return {'message':'item deleted'}
    
    @jwt_required()
    def put(self,name):
        data = Item.parser.parse_args()
        item = next(filter(lambda c:c['name']==name,items),None)
        if item is None:
            item = {'name':name,'price':data['price']}
            items.append(item)
        else:
            items.update(data)
        return item

class Items(Resource):
    @jwt_required()
    def get(self):
        return items



api.add_resource(Item,'/item/<string:name>') # http://127.0.0.1:5000/student/<string:name>
api.add_resource(Items,'/items')
app.run(port=5000)

