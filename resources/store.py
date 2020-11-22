from flask_restful import Resource
from models.stores import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store is None:
            return {"message":"Store not found"}
        
        return store.json()

    def post(self,name):
        store = StoreModel.find_by_name(name)
        if store is None:
            store = StoreModel(name)
            store.save_to_db()
            return store.json()
        return {"message":"Store {} is already existed".format(name)}

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store is None:
            return {"message":"{} not found".format(name)}
        store.delete()
        return {"message":"{} is deleted".format(name)}

class StoreList(Resource):
    def get(self):
        return {"store":[x.json() for x in StoreModel.query.all()]}