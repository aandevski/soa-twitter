import os
from flask import Flask
import consul

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# consul.register()


import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Tweet


@app.route("/")
def hello():
    return "Hello from Tweets!"


@app.route("/add",methods=['POST','GET'])
def add_tweet():
    name = request.args.get('name')
    author = request.args.get('author')
    published = request.args.get('published')
    try:
        tweet = Tweet(
            name=name,
            author=author,
            published=published
        )
        db.session.add(tweet)
        db.session.commit()
        return "Tweet added. tweet id={}".format(tweet.id, tweet.author,tweet.name)
    except Exception as e:
        return (str(e))


@app.route("tweets/getall")
def get_all():
    try:
        tweets = Tweet.query.all()
        return jsonify([e.serialize() for e in tweets])
    except Exception as e:
        return (str(e))


@app.route("tweets/get/<id_>")
def get_by_id(id_):
    try:
        tweet = Tweet.query.filter_by(id=id_).first()
        return jsonify(tweet.serialize())
    except Exception as e:
        return (str(e))


if __name__ == '__main__':
    app.run()
