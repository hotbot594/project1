import sqlite3
from flask_login import login_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from models import *
from sqlalchemy.orm import declarative_base, Session
import secrets

DATABASE_URI = '../app.db'
login_manager = LoginManager()
session = Session()
connection = sqlite3.connect('app.db', check_same_thread=False)
cursor = connection.cursor()

def register_user(username: str) -> User | None:
    password = secrets.token_urlsafe(8)
    hashed_password = generate_password_hash(password)
    user = User(name=username, password=hashed_password)

    err = add_object_to_database(user)
    if err:
        print(err)
        return None, None
    return user, password



def login(username, password):
    user = session.query(User).filter_by(username=username).first()

    if user:
        if check_password_hash(user.password, password):
            login_user(user)
            return 'success'
        else:
            return 'passwords don\'t match'
    else:
        return 'user doesn\'t exist'





def get_object_by_id(obj_id, class_name):
    obj = session.query(class_name).where(class_name.id == obj_id).first()
    return obj

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(int(user_id))

def add_object_to_database(obj: object):
    try:
        session.add(obj)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        return 'err'