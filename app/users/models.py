import enum
from app import db

from flask import abort, current_app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.exc import IntegrityError
from app.utils.custom_exception import DbException
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer,
    BadSignature,
    SignatureExpired,
)


class MyEnum(enum.Enum):
    superuser = 1
    adminuser = 2
    normaluser = 3


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String)
    email_address = db.Column(db.String(50), unique=True)
    user_type = db.Column(db.Enum(MyEnum), default="normaluser")
    contacts = db.relationship(
        "Contact", back_populates="user", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return "<User (username = {}, user_type={})>".format(self.username, self.user_type)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        self.check_password_hash = check_password_hash(self.password_hash, password)

    def is_active(self):
        return True

    def get_id(self):
        return self.email_address

    def generate_auth_token(self, expiration=600):
        s = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)
        return s.dumps({"id": self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data["id"])
        return user

    def save(self, data):
        self.username = data["username"]
        self.password_hash = self.set_password(data["password"])
        self.email_address = data["email_address"]
        self.user_type = data.get("user_type", "normaluser")
        if User.query.filter_by(username=self.username).first() is not None:
            raise DbException("Username already Exist")
        if User.query.filter_by(email_address=self.email_address).first() is not None:
            raise DbException("Email already Exist")
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError:
            raise DbException("Something went wrong with data base.")

        return self

    def get_all(self):
        return User.query.all()

    def get(self, id):
        return User.query.filter_by(id=id).first()


class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="contacts")

    def __repr__(self):
        return "<Contact (Full name = {} {}, email = {})>".format(
            self.first_name, self.last_name, self.email_address
        )
