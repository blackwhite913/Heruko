import sqlite3
from sqlite3.dbapi2 import connect
from db import db

class User(db.Model):
    #telling the SQLAlchemy object number of columns and the table to look for
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))



    # python constructor for class User
    def __init__(self,username,password):
        self.password=password
        self.username = username
    
    @classmethod
    def find_by_username(cls,username):
        # cls.query = SELECT * FROM users
        return cls.query.filter_by(username=username).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
       