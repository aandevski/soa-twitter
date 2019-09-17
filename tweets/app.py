import os

import consul
from flask import Flask, request, jsonify

from db import db
from models import Tweet

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db.init_app(app)
consul.register()


@app.route("/add", methods=['POST'])
def add_tweet():
    name = request.json.get('name')
    author = request.json.get('author')
    published = request.json.get('published')
    try:
        tweet = Tweet(
            name=name,
            author=author,
            published=published
        )
        db.session.add(tweet)
        db.session.commit()
        return "Tweet added. tweet id={}".format(tweet.id, tweet.author, tweet.name)
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
