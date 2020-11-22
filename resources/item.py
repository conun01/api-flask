from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemsModel
from flask import jsonify



class Item(Resource):
    TABLE_NAME = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store_id"
    )



    def get(self, name):
        item = ItemsModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemsModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()
        print(data['price'])
        print(data['store_id'])
        item = ItemsModel(name, data['price'],data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}

        return item.json(), 201

 
    def delete(self, name):
        item = ItemsModel.find_by_name(name)
        if item:
            item.delete()
            return {'message': 'Item deleted'}
        else:
            return {"message":"{} not found to delete".format(name)}


    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemsModel.find_by_name(name)
        if item is None:
            try:
                item = ItemsModel(name, data['price'], data['store_id'])
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                item.price = data['price']
            except:
                return {"message": "An error occurred updating the item."}
        item.save_to_db()
        return item.json()


class ItemList(Resource):

    def get(self):
        item = ItemsModel.query_all_in_table()
        
        return {"item":[x.json() for x in item]}
