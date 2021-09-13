import sqlite3
from sqlite3.dbapi2 import connect
from flask_restful import Resource,reqparse
from models.user import User

class UserRegister(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('username',type=str,required=True)
        parser.add_argument('password',type=str,required=True)
        data=parser.parse_args()
        val=User.find_by_username(data["username"])
        if val is None:
            val=User(**data)
            val.save_to_db()
            return {"message":"Username Created successfully"},200
        else:
            return {"message":"Username already exists"},201

