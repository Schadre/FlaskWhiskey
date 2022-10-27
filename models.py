from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets

login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first = db.Column(db.String(150), nullable=True, default='')
    last = db.Column(db.String(150), nullable = True, default ='')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default ='')
    token = db.Column(db.String, default = '', unique = True )
    g_auth_verify = db.Column(db.Boolean, default = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, first='', last='', email='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first = first
        self.last = last
        self.email = email
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'

class Whiskey(db.Model):
    id = db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    style = db.Column(db.String(200))
    age = db.Column(db.String(20))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, name, style, age, user_token, id=''):
        self.id = self.set_id()
        self.name = name
        self.style = style
        self.age = age
        self.user_token = user_token


    def __repr__(self):
        return f'The following has been added to the database: {self.age} {self.name} {self.style}'

    def set_id(self):
        return (secrets.token_urlsafe())

class WhiskeySchema(ma.Schema):
    class Meta:
        fields = ['Id', 'Name', 'Style', 'Age']

whiskey_schema = WhiskeySchema()
whiskeys_schema = WhiskeySchema(many=True)