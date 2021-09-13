from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message":"The store does not exist"},404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message":"store already exists"}
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message":"Error occurred"},500
        return {"message":"store created successfully"},200

        

    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_from_db(name)
                return {"message":"store deleted successfully"},200
            except:
                return {"message":"Error occurred"},500
        return {'message':"store does not exist"},404
            


class StoreList(Resource):
    def get(self):
        return {"stores":list(map(lambda x:x.json(),StoreModel.query.all()))}