from app.marshmallow_schema import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "email_address", "_links")

    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("users.user_details", id="<id>"),
            "collections": ma.URLFor("users.all_users"),
        }
    )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
