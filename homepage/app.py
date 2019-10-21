import os
from flask import Flask, jsonify
import consul

from service import user_required, check_user_existence, get_followings_of_user, get_tweets_by_user

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig'))

if not app.config['DEBUG']:
    consul.register()


@app.route("/")
@user_required
def get_homepage(user):
    try:
        check_user_existence(user['id'])
        followings = get_followings_of_user(user['id'])
        tweets = [get_tweets_by_user(following['following_id']) for following in followings]
        collected_tweets = []
        [collected_tweets.extend(tweet) for tweet in tweets]
        return jsonify(collected_tweets)
    except Exception as e:
        return str(e)
