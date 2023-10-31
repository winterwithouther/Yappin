from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

class Post(db.Model, SerializerMixin):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    caption = db.Column(db.String)

    comments = db.relationship("Comment", backref="post", cascade="all, delete-orphan")
    likes = db.relationship("Like", backref="post", cascade="all, delete-orphan")

    serialize_rules = ("-comments.post", "-likes.post",)

class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    comments = db.relationship("Comment", backref="user", cascade="all")
    likes = db.relationship("Like", backref="user", cascade="all, delete-orphan")

    serialize_rules = ("-comments.user", "-likes.user",)

class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)

    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    serialize_rules = ("-post.comments", "-user.comments",)

class Like(db.Model, SerializerMixin):
    __tablename__ = "likes"
    id = db.Column(db.Integer, primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    serialize_rules = ("-post.likes", "-user.likes",)

