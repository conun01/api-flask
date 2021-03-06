from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity

from db import db
from resources.user import UserRegister, GetAllUser
from resources.item import Item, ItemList
from resources.store import Store, StoreList

import os

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(GetAllUser, '/users')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True,host="0.0.0.0",port="7878")  # important to mention debug=True
