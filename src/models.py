from flask_sqlalchemy import SQLAlchemy
from typing import List
from sqlalchemy import String, Boolean, Integer, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_from_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_from:  Mapped["User"] = relationship(back_populates = "followers_from")

    user_to_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user_to:  Mapped["User"] = relationship(back_populates = "followers_to")

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    followers_from: Mapped[List["Follower"]] = relationship(
        back_populates="user_from", foreign_keys=[Follower.user_from_id]
    )
    followers_to: Mapped[List["Follower"]] = relationship(
        back_populates="user_to", foreign_keys=[Follower.user_to_id]
    )

    comments: Mapped[List["Comment"]] = relationship(back_populates = "author")

    posts: Mapped[List["Post"]] = relationship(back_populates = "user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), nullable=False)

    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship(back_populates = "comments")

    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship(back_populates = "comments")



class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    comments: Mapped[List["Comment"]] = relationship(back_populates = "post")

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates = "posts")

    medias: Mapped[List["Media"]] = relationship(back_populates="post")


class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(120), nullable=False)
    url: Mapped[str] = mapped_column(String(120), nullable=False)

    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
    post: Mapped["Post"] = relationship(back_populates="medias")
