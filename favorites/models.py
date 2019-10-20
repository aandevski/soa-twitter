from db import db
import datetime


class Favorite(db.Model):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    tweet_id = db.Column(db.Integer)
    favorited_at = db.Column(db.DateTime())

    def __init__(self, user_id, tweet_id):
        self.user_id = user_id
        self.tweet_id = tweet_id
        self.favorited_at = datetime.datetime.utcnow()

    def __repr__(self):
        return f'U{self.user_id} favs T{self.tweet_id}'

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'tweet_id': self.tweet_id,
            'favorited_at': self.favorited_at
        }
