from db import db


class Tweet(db.Model):
    __tablename__ = 'tweets'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    author = db.Column(db.String())
    published_at = db.Column(db.DateTime())

    def __init__(self, text, author, published_at):
        self.text = text
        self.author = author
        self.published_at = published_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'text': self.text,
            'author': self.author,
            'published_at': self.published_at
        }
