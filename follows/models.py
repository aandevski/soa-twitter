from db import db
from sqlalchemy import UniqueConstraint


class Following(db.Model):
    __tablename__ = 'following'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer)
    following_id = db.Column(db.Integer)
    followed_at = db.Column(db.DateTime())

    __table_args__ = (UniqueConstraint('follower_id', 'following_id', name='_follower_following_uc'),
                      )

    def __init__(self, follower_id, following_id, followed_at):
        self.follower_id = follower_id
        self.following_id = following_id
        self.followed_at = followed_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'follower_id': self.follower_id,
            'following_id': self.following_id,
            'followed_at': self.followed_at
        }
