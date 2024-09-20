import mongoengine as me
from flask_mongoengine import MongoEngine
from .users import User 
from .courses import Course
__all__ = []


db = MongoEngine()


def init_db(app):
   db.init_app(app)
