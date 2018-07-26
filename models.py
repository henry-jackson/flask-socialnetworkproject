import datetime

from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash, check_password_hash
from peewee import *

DATABASE = SqliteDatabase('social.db')

# Model going second means the class is ultimately a Model
class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at', )

    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            cls.create(
                username=username,
                email=email,
                password=password,
                is_admin=admin,
            )
        except IntegrityError:
            raise ValueError("User already exists")