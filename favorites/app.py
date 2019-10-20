import os
from flask import Flask, jsonify
import consul

from db import db
from models import Favorite
from service import user_required, check_user_existence, check_tweet_existence, get_tweet, get_user

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig'))

db.init_app(app)
if not app.config['DEBUG']:
    consul.register()


@app.route("/user/<id_>")
def get_favorite_tweets_of_user(id_):
    try:
        check_user_existence(id_)
        favorites = Favorite.query.filter_by(user_id=id_).all()
        tweets = [get_tweet(favorite.tweet_id) for favorite in favorites]
        return jsonify(tweets=tweets)
    except Exception as e:
        return str(e)


@app.route("/tweet/<id_>")
def get_users_favoriting_tweet(id_):
    try:
        check_tweet_existence(id_)
        favorites = Favorite.query.filter_by(tweet_id=id_).all()
        users = [get_user(favorite.user_id) for favorite in favorites]
        return jsonify(users=users)
    except Exception as e:
        return str(e)


@app.route("/tweet/<id_>", methods=('POST', ))
@user_required
def set_tweet_as_favorite(user, id_):
    try:
        check_tweet_existence(id_)
        new_fav = Favorite(user_id=user['id'], tweet_id=id_)
        db.session.add(new_fav)
        db.session.commit()
        return jsonify(success=True), 201
    except Exception as e:
        return str(e)
