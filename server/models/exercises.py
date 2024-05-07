from config import db
import ipdb

# class Exercises(db.Model):
#     pass

class Test:
    def goofin(self):
        print('goofin off')

class Activity(Test):
    __tablename__ = 'Activities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

ipdb.set_trace()