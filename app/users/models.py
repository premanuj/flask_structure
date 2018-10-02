import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class MyEnum(enum.Enum):
    superuser = 1
    adminuser = 2
    normaluser = 3


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String)
    email_address = db.Column(db.String)
    user_type = db.Column(db.Enum(MyEnum))
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

    def save(self, data):
        self.username = data["username"]
        self.password_hash = self.set_password(data["password"])
        self.email_address = data["email_address"]

        sql = db.session.add(self)
        print("SQL", self)
        db.session.commit()
        print(sql)
        return self.get_id()

    def get_all(self):
        return User.query.all()


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
