from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    username = db.Column(db.String())
    date_published = db.Column(db.String())

    def __init__(self, name, username, date_published):
        self.name = name
        self.username = username
        self.date_published = date_published

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.username,
            'published': self.date_published
        }
