import os
from datetime import datetime

import consul
from flask import Flask, request, jsonify

from db import db
from models import Tweet

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig'))

db.init_app(app)
if not app.config['DEBUG']:
    consul.register()


@app.route("/add", methods=['POST'])
def add_tweet():
    text = request.json.get('text')
    author = request.json.get('author')
    published_at = datetime.now()
    try:
        tweet = Tweet(
            text=text,
            author=author,
            published_at=published_at
        )
        db.session.add(tweet)
        db.session.commit()
        return jsonify(success=True), 201
    except Exception as e:
        return (str(e))


@app.route("/")
def get_all():
    try:
        tweets = Tweet.query.all()
        return jsonify([e.serialize() for e in tweets])
    except Exception as e:
        return (str(e))


@app.route("/<id_>")
def get_by_id(id_):
    try:
        tweet = Tweet.query.filter_by(id=id_).first()
        return jsonify(tweet.serialize())
    except Exception as e:
        return (str(e))


if __name__ == '__main__':
    app.run()
