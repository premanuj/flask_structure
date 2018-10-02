import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app import db


class MyEnum(enum.Enum):
    superuser = 1
    adminuser = 2
    normaluser = 3


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)
    user_type = db.Column(db.Enum(MyEnum))
    contacts = db.relationship(
        "Contact", back_populates="user", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return "<User (username = {}, user_type={})>".format(self.username, self.password)


class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="contacts")

    def __repr__(self):
        return "<Contact (Full name = {} {}, email = {})>".format(
            self.first_name, self.last_name, self.email_address
        )
