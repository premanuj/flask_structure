
from app.marshmallow_schema import ma
from marshmallow import fields, post_load, Schema
from app.users.models import User


class UserSchema(Schema):
    username = fields.String(required=True, error_messages={"messages": "Username is required."})
    email_address = fields.Email(required=True, error_messages={"messages": "Email is required."})
    password = fields.String(required=True, error_messages={"messages": "Password is required."})
    user_type = fields.String()

    class Meta:
        fields = ("id", "username", "email_address", "_links", "password", "user_type", "contacts")

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("users.user_details", id="<id>"),
            "collections": ma.URLFor("users.all_users"),
        }
    )


class UserProfileSchema(Schema):
    first_name = fields.String(
        required=True, error_messages={"messages": "First name is required."}
    )
    last_name = fields.String(required=True, error_messages={"messages": "Last name is required."})
    user_id = fields.Integer(required=True, error_messages={"messages": "Password is required."})

    class Meta:
        fields = ("id", "first_name", "last_name", "user_id")


profile_schema = UserProfileSchema()
profiles_schema = UserProfileSchema(many=True)


user_schema = UserSchema()
users_schema = UserSchema(many=True)
